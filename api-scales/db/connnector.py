import mysql.connector
from decouple import config

mysql_config = {
    'user': config('DATABASE_USER'),
    'password': config('DATABASE_PASSWORD'),
    'host': config('DATABASE_HOST'),
    'database': config('DATABASE_NAME')
}
db_connection = mysql.connector

def get_table(table: str):
    try:
        connection = db_connection.connect(**mysql_config)
        if connection.is_connected():
            cursor = connection.cursor()

            # query = f'SELECT name, plu, price FROM {table}'
            #query = f"SELECT * FROM {table}"
            query = f"SELECT name, plu, CAST(price AS CHAR(10)) AS formatted_price FROM {table}"

            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return rows
            else:
                return None
    except mysql.connector.Error as err:
        raise err
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()