import sqlite3 as sql

dbnombre = "database.db"
def insertarusuario(usuario: str, psw: str):
    with sql.connect(dbnombre) as conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO usuario(user, password) VALUES (?, ?)", (usuario, psw))
            cur.close()
        except Exception:
            raise Exception("El usuario ya existe")

def buscarusuario(usuario: str, psw: str):
    with sql.connect(dbnombre) as conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM usuario WHERE user = ? AND password = ?", (usuario, psw))
            res = cur.fetchall()
            if (len(res) < 1):
                raise Exception("Usuario no encontrado")
            
            return res
        except Exception as e:
            raise Exception("Error al buscar el usuario", str(e))