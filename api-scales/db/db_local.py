import sqlite3

# Conectar a la base de datos o crearla si no existe
conexion = sqlite3.connect("db_local.db")

# Crear la tabla "items" si no existe
try:
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            plu TEXT,
            precio REAL
        );
    """)
    print("Se creó la tabla 'items'")
except sqlite3.OperationalError:
    print("La tabla 'items' ya existe")

# Cerrar la conexión a la base de datos
conexion.close()
