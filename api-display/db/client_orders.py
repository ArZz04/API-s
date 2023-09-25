import mysql.connector
import sqlite3

# Configuración de MySQL
mysql_config = {
    'user': 'pcscale',
    'password': 'epelsa',
    'host': '192.168.100.212',
    'database': 'pcscale'
}

# Intenta establecer la conexión a MySQL
try:
    connection = mysql.connector.connect(**mysql_config)
    if connection.is_connected():
        print('Conexión establecida a la base de datos MySQL')

        # Crea un cursor para ejecutar consultas en MySQL
        cursor = connection.cursor()

        # Obtiene la descripción de las columnas de la tabla 'lcustomerorders' en MySQL
        query_columns = "DESCRIBE lcustomerorders"
        cursor.execute(query_columns)
        columns_data = cursor.fetchall()

        # Obtiene la primera fila de contenido de la tabla 'lcustomerorders' en MySQL
        query_first_row = "SELECT * FROM lcustomerorders LIMIT 1"
        cursor.execute(query_first_row)
        first_row_data = cursor.fetchone()

        if columns_data and first_row_data:
            column_names = [column[0] for column in columns_data]
            formatted_output = {column: value for column, value in zip(column_names, first_row_data)}
            print("Datos de MySQL:")
            print(formatted_output)

            # Conexión a SQLite y almacenamiento de datos
            sqlite_connection = sqlite3.connect('mysql_data.db')
            sqlite_cursor = sqlite_connection.cursor()

            # Crear una tabla en SQLite con la misma estructura que la de MySQL
            create_table_sql = f"CREATE TABLE IF NOT EXISTS lcustomerorders ({', '.join([f'{column} TEXT' for column in column_names])})"
            sqlite_cursor.execute(create_table_sql)

            # Insertar los datos de MySQL en SQLite
            insert_sql = f"INSERT INTO lcustomerorders ({', '.join(column_names)}) VALUES ({', '.join(['?' for _ in column_names])})"
            sqlite_cursor.execute(insert_sql, first_row_data)
            sqlite_connection.commit()

            print('Datos almacenados en SQLite')

except mysql.connector.Error as err:
    print(f'Error de MySQL: {err}')
except sqlite3.Error as err:
    print(f'Error de SQLite: {err}')
finally:
    # Cierra los cursores y conexiones cuando hayas terminado
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print('Conexión a MySQL cerrada')
    if 'sqlite_cursor' in locals():
        sqlite_cursor.close()
    if 'sqlite_connection' in locals():
        sqlite_connection.close()
        print('Conexión a SQLite cerrada')
