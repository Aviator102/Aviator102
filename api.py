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
    try:
        connection = conectar_bd()
        if connection is None:
            print("Erro: Conexão com o banco de dados não estabelecida.")
            return jsonify({"error": "Erro de conexão com o banco de dados"}), 500

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, valor, hora FROM resultados ORDER BY id DESC LIMIT 100")
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(resultados)
    except Exception as e:
        print(f"Erro durante a execução da API: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
