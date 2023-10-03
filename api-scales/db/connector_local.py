import sqlite3

def create_connection():
    conn = sqlite3.connect('db_local.db')  # Nombre de la base de datos
    return conn

def execute_query(conn, query, params=None):
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()