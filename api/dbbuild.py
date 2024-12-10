import sqlite3

with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()
    try:
        # Intentar crear la tabla solo si no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario(
                user TEXT PRIMARY KEY,
                password TEXT
            )
        """)
    except Exception as e:
        print("Hubo un error al intentar crear una tabla:", e)
    else:
        print("Tabla creada correctamente (o ya existía)")
