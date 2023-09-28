import mysql.connector

# Configuración de MySQL
mysql_config = {
    'user': 'pcscale',
    'password': 'epelsa',
    'host': '192.168.100.212',
    'database': 'pcscale'
}

# Función para obtener los valores de una tabla específica en MySQL
def obtener_valores_de_tabla(tabla):
    try:
        connection = mysql.connector.connect(**mysql_config)
        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta para obtener solo los campos 'name', 'plu' y 'price' de la tabla específica
            query = f"SELECT name, plu, price FROM {tabla}"
            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                return rows
            else:
                print(f"La tabla '{tabla}' está vacía.")

    except mysql.connector.Error as err:
        print(f'Error de MySQL: {err}')
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Intenta establecer la conexión a MySQL
try:
    connection = mysql.connector.connect(**mysql_config)
    if connection.is_connected():
        print('Conexión establecida a la base de datos MySQL')

        # Crea un cursor para ejecutar consultas en MySQL
        cursor = connection.cursor()

        # Obtiene las tablas en la base de datos MySQL
        query_tables = "SHOW TABLES"
        cursor.execute(query_tables)
        tables = cursor.fetchall()

        if tables:
            print("Tablas en la base de datos MySQL:")
            for table in tables:
                print(table[0])

            # Llama a la función para obtener los valores de la tabla 'items'
            tabla_a_consultar = 'items'
            valores_items = obtener_valores_de_tabla(tabla_a_consultar)

            if valores_items:
                print(f"Valores de la tabla '{tabla_a_consultar}':")
                for row in valores_items:
                    print(row)

            # Llama a la función para obtener los valores de la tabla 'vendors'
            tabla_a_consultar = 'vendors'
            valores_vendors = obtener_valores_de_tabla(tabla_a_consultar)

            if valores_vendors:
                print(f"Valores de la tabla '{tabla_a_consultar}':")
                for row in valores_vendors:
                    print(row)

except mysql.connector.Error as err:
    print(f'Error de MySQL: {err}')
finally:
    # Cierra el cursor y la conexión cuando hayas terminado
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Conexión a MySQL cerrada')