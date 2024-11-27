import mysql.connector

# Configuração para conectar ao MySQL via XAMPP
db_config = {
    'host': 'localhost',        # Endereço do servidor MySQL
    'user': 'root',             # Usuário padrão do XAMPP
    'password': '',             # Senha (geralmente vazia no XAMPP)
    'database': 'assistente'    # Nome do banco de dados
}

def criar_tabela():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aprendizado (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pergunta TEXT UNIQUE NOT NULL,
            resposta TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_resposta(pergunta, resposta):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO aprendizado (pergunta, resposta) VALUES (%s, %s)", (pergunta, resposta))
        conn.commit()
    except mysql.connector.errors.IntegrityError:
        pass  # Pergunta já existe
    conn.close()

def obter_resposta(pergunta):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT resposta FROM aprendizado WHERE pergunta = %s", (pergunta,))
    resposta = cursor.fetchone()
    conn.close()
    if resposta:
        return resposta[0]
    return None
