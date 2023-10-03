from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from db.connnector import get_table 
from db.connector_local import create_connection, execute_query

from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes ajustar esto para permitir solo un dominio específico si es necesario
    allow_methods=["*"],  # Puedes limitar los métodos HTTP permitidos si es necesario
    allow_headers=["*"],  # Puedes limitar los encabezados permitidos si es necesario
)

@app.get('/')
def main_route():
    return {"API-STATE": "WORKS"}

#GETS
@app.get('/mysql/refreshItems') # TRAER DATOS DE BASE DATOS DE BASCULA
async def get_table():
    try:
        conn = create_connection()

        table_data = get_table('items')

        # Define la consulta SQL para insertar datos en la tabla
        query = "INSERT INTO items (nombre, plu, precio) VALUES (?, ?, ?)"

        # Itera a través de los datos de la tabla y ejecuta la consulta SQL
        for row in table_data:
            execute_query(conn, query, row)

        conn.close()

        return table_data

    except Exception as e:
        return {"error": f"Connection with table items has failed: {str(e)}"}
    
@app.get('/sqlite/items', response_model=List[dict]) # RETORNAR BASE DE DATOS LOCAL
async def return_table():
    try:
        conn = create_connection()

        cursor = conn.execute("select nombre, plu, precio from items")

        json_returned = []

        for fila in cursor:
            nombre, plu, precio = fila
            json_returned.append({
                "nombre": nombre,
                "plu": plu,
                "precio": precio
            })

        conn.close()
        json_returned.pop(0)
        return json_returned
        
    except Exception as e:
        print(f"Error: {str(e)}")

# ORDENAR POR PLU, NOMBRE, PRECIO, FAMILIA
@app.get('/itemsOrdered', response_model=List[dict])
async def return_table_ordered(order_by: str = Query(default="plu"), order_dir: str = Query(default="asc")):
    try:
        conn = create_connection()

        # Validar que el campo de orden sea válido (plu, nombre, precio, familia)

        #if order_by not in ["plu", "nombre", "precio", "familia"]:
        if order_by not in ["plu", "nombre", "precio"]:
            return {"error": "Campo de orden no válido"}

        # Validar que la dirección del orden sea válida (asc o desc)
        if order_dir not in ["asc", "desc"]:
            return {"error": "Dirección de orden no válida"}

        # Crear una consulta SQL dinámica basada en el campo de orden y dirección especificados
        #query = f"SELECT nombre, plu, precio, familia FROM items ORDER BY {order_by} {order_dir}"
        query = f"SELECT nombre, plu, precio FROM items ORDER BY {order_by} {order_dir}"

        cursor = conn.execute(query)

        json_returned = []

        for fila in cursor:
            # nombre, plu, precio, familia = fila  //DESCOMENTAR CUANDO YA SE TENGA LA FAMILIA EN LA DB LOCAL
            nombre, plu, precio = fila
            json_returned.append({
                "nombre": nombre,
                "plu": plu,
                "precio": precio,
                # "familia": familia
            })

        conn.close()
        json_returned.pop(0)
        return json_returned

    except Exception as e:
        print(f"Error: {str(e)}")

# EDITAR INDIVIDUAL


# BUSCAR POR PLU, NOMBRE, FAMILIA
@app.get('/search', response_model=List[dict])
async def search_items(
    query: str = Query(..., description="Término de búsqueda (PLU, nombre o familia)")
):
    try:
        conn = create_connection()

        # Consulta SQL para buscar en PLU, nombre o familia
        query_sql = (
            "SELECT nombre, plu, precio FROM items "
            "WHERE plu LIKE ? OR nombre LIKE ?"
            #"WHERE plu LIKE ? OR nombre LIKE ? OR familia LIKE ?"
        )

        cursor = conn.execute(query_sql, (f"%{query}%", f"%{query}%"))

        json_returned = []

        for fila in cursor:
            #nombre, plu, precio, familia = fila
            nombre, plu, precio = fila
            json_returned.append({
                "nombre": nombre,
                "plu": plu,
                "precio": precio,
                #"familia": familia
            })

        conn.close()

        return json_returned

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


