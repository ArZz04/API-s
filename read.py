import sqlite3

conexion=sqlite3.connect("db_local.db")
cursor=conexion.execute("select nombre, plu, precio from items")
for fila in cursor:
    print(fila)
conexion.close()