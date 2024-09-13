from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    return mysql.connector.connect(
        host='db4free.net',
        user='ssonhador',
        password='ssonhador',
        database='ssonhador'
    )

# Rota da API para retornar os resultados como JSON
@app.route('/api/resultados', methods=['GET'])
def api_resultados():
    connection = conectar_bd()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, valor, hora FROM resultados ORDER BY id DESC LIMIT 100")
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
