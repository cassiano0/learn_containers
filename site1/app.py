import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='db',  # Este é o nome do serviço do PostgreSQL no docker-compose
        database='meu_app',
        user='user',
        password='password'
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT 1')  # Apenas um teste para verificar a conexão
    result = cur.fetchone()
    cur.close()
    conn.close()
    return f"Conexão com o banco de dados bem-sucedida!! {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
