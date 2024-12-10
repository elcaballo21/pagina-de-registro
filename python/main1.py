from flask import Flask, render_template,request, jsonify
from modulos import fechas as f
import requests
import hashlib
import datetime as dt
import os
from dotenv import load_dotenv
import sqlite3

dbnombre = "database.db"

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Flask está funcionando!"

@app.route("/bienvenida")
def bienvenida():
    fechahoy = f.obtenerfecha()
    return f"<p>{fechahoy}</p>"

@app.route("/blog")
def mipagina():
    return render_template("blog.html")

@app.route("/api")
def api():
    response = requests.get("https://www.swapi.tech/api/starships/9")
    data = response.json()
    model = data["result"]["properties"]["model"]
    return f"model = {model}"

@app.route("/ApiMarvelTest/<personaje>")
def ApiMarvel(personaje):
    publicKey = "f334cf55497ba0b9ba814fdf2ee3a3e6"
    privateKey = os.getenv("MARVEL_PRIVATE_KEY")  # Leer clave desde una variable de entorno

    if not privateKey:
        return "Error: Clave privada no configurada.", 500

    now = dt.datetime.now()
    timestamp = int(round(now.timestamp()))

    # Generar hash siguiendo el formato indicado
    hashString = f"{timestamp}{privateKey}{publicKey}"
    hashMd5 = hashlib.md5(hashString.encode())

    response = requests.get(
        "https://gateway.marvel.com/v1/public/characters",
        params={
            "nameStartsWith": personaje,
            "apikey": publicKey,
            "hash": hashMd5.hexdigest(),
            "ts": timestamp,
        },
        verify=True 
    )
    return response.json()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        usuario = request.form['usuario']
        psw = request.form['psw']
        data = {"usuario": usuario, "psw": psw}
        # Enviar datos a la API
        response = requests.post("http://127.0.0.1:5001/IniciarSesion", json=data)
        return response.json()
        
    #     with sqlite3.connect(dbnombre) as conn:
    #         cur = conn.cursor()
    #         cur.execute('SELECT * from usuario WHERE user=(?)', (nombre,))
    #         respuestaDb = cur.fetchall()
    # if respuestaDb == []:
    #     return "<h1>No existe el usuario<h1>"
    # else:
    #     return "<h1>Existe<h1>"

        
    
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "GET":
        return render_template("Formregistro.html")
    elif request.method == "POST":
        usuario = request.form['usuario']
        psw = request.form['psw']
        data = {"usuario": usuario, "psw": psw}
        # Enviar datos a la API
        response = requests.post("http://127.0.0.1:5001/Ingreseusuario", json=data)
        return response.content, response.status_code

        
    
        print(f"Nombre: {nombre}, Contraseña: {psw}")

        # with sqlite3.connect(dbnombre) as conn:
        #     cur = conn.cursor()
        #     try:
        #         cur.execute("INSERT INTO usuario(user, password) VALUES (?, ?)", (nombre, psw))
            
        #     except sqlite3.IntegrityError as e:
        #         return f"<h1>El nombre de usuario ya se encuentra en uso</h1><p>{str(e)}</p><a href='/registro'>Volver al registro</a>"
        #     except Exception as e:
        #         return f"<h1>Error al cargar el usuario</h1><p>{str(e)}</p><a href='/registro'>Volver al registro</a>"
        #     else:
        #         return "<h1>Usuario cargado exitosamente</h1><a href='/login'>Ir al login</a>"










    

if __name__ == "__main__":
    app.run(debug=True)
