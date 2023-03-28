from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def consulta():
    conn = sqlite3.connect('victoryapi.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM boxeador;')
    datos = cursor.fetchall()
    conn.close()

    resultado = []
    for dato in datos:
        dict_dato = {}
        dict_dato['id'] = dato[0]
        dict_dato['nombre'] = dato[1]
        dict_dato['nacionalidad'] = dato[2]
        resultado.append(dict_dato)

    return jsonify(resultado)


if __name__ == '__main__':
    app.run()