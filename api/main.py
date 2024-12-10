from flask import Flask, jsonify, request
import dblib as db
import sqlite3


app = Flask(__name__)



@app.route('/')
def api():
    return "api"

# @app.route('/comoseveunjson')
# def comoseveunjson():
#     data = {}
#     data.setdefault("nombre", "Lautaro")
#     data.setdefault("apellido", "Puertas")
#     return jsonify(data), 401

@app.route("/Ingreseusuario", methods=["POST"])
def ingreseusuario():
    try:
        data = request.get_json()
        usuario = data["usuario"]
        psw = data["psw"]
        db.insertarusuario(usuario, psw)
        return jsonify({}),200
    except Exception as e:
        return str(e), 400
    

@app.route("/IniciarSesion", methods=["POST"])
def iniciarsession():
    try:
        data = request.get_json()
        usuario = data["usuario"]
        psw = data["psw"]
        db.buscarusuario(usuario, psw)
        data = dict(mensaje='Usuario encontrado')
        return jsonify(data), 200
    except Exception as e:
        return str(e), 401
