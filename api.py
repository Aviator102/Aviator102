from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def conectar_bd():
    try:
        return mysql.connector.connect(
            host='db4free.net',
            user='ssonhador',
            password='ssonhador',
            database='ssonhador'
        )
    except Error as e:
        print(f"Erro de conexão: {e}")
        return None

@app.route('/api/resultados', methods=['GET'])
def api_resultados():
    connection = conectar_bd()
    if connection is None:
        return jsonify({"error": "Erro de conexão com o banco de dados"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, valor, hora FROM resultados ORDER BY id DESC LIMIT 100")
        resultados = cursor.fetchall()
        return jsonify(resultados)
    except Error as e:
        return jsonify({"error": f"Erro ao consultar o banco de dados: {e}"}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
