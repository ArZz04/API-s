
from fastapi import FastAPI, Depends, HTTPException

import mysql.connector
from env.variables import user, password, host, database

mysql_config = {
    'user' : user,
    'password' : password,
    'host' : host,
    'database' : database
}

db_connection = mysql.connector

def get_table(table):
    try:
        connection = db_connection.connect(**mysql_config)

        if connection.is_connected():
            cursor = connection.cursor()

            #query = f'SELECT name, plu, price FROM {table}'
            query = f"SELECT name, plu, CAST(price AS CHAR(10)) AS formatted_price FROM {table}"

            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                return rows
            else:
                raise HTTPException(status_code=404, detail=f'The table "{table}" is empty')

    except db_connection.Error as err:
        raise HTTPException(status_code=500, detail=f'Server error: {err}')
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()