from fastapi import FastAPI, Depends, HTTPException, Path
import mysql.connector
from env.variables import user, password, host, database

app = FastAPI()

mysql_config = {
    'user': user,
    'password': password,
    'host': host,
    'database': database
}

db_connection = mysql.connector


def get_table(table: str = Path(..., title="Table Name")):
    try:
        connection = db_connection.connect(**mysql_config)
        if connection.is_connected():
            cursor = connection.cursor()

            # query = f'SELECT name, plu, price FROM {table}'
            query = f"SELECT name, plu, CAST(price AS CHAR(10)) AS formatted_price FROM {table}"

            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return rows
            else:
                raise HTTPException(
                    status_code=404, detail=f'The table "{table}" is empty')
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f'Server error: {err}')
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


@app.get('/')
def main_route():
    return {"API-STATE": "WORKS"}


@app.get('/table/{table}', response_model=list[list[str]])
async def get_table_endpoint(table: str = Depends(get_table)):
    return table

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
