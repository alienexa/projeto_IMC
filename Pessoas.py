import sqlite3

# Criação da tabela de PESSOAS
def cria_tabela_pessoas():
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(
                            pessoa_id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            age INTEGER,
                            height REAL,
                            weight REAL,
                            user_id INTEGER,
                            FOREIGN KEY(user_id) REFERENCES users(user_id))''')
    connect.commit()
    connect.close()

#Operações CRUD para PESSOAS: CREATE pessoas | READ pessoas | UPDATE pessoas | DELETE pessoas

#CREATE pessoas
def regista_pessoa(first_name, last_name, age, height, weight, user_id):
    connect = sqlite3.connect('bmi.db')
    connect.cursor().execute(
        'INSERT INTO pessoas (first_name, last_name, age, height, weight, user_id) VALUES (?, ?, ?, ?, ?, ?)',
        (first_name, last_name, age, height, weight, user_id))
    connect.commit()
    connect.close()

#READ pessoas
def ler_pessoas():
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM pessoas')
    pessoas = cursor.fetchall()
    connect.close()
    return pessoas

def ler_pessoas_por_nome(user_id: int, first_name):
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM pessoas WHERE user_id=? AND first_name=?', (user_id,first_name,))
    pessoas = cursor.fetchall()
    connect.close()
    return pessoas

def ler_pessoa(first_name):
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users WHERE first_name=?',(first_name,))
    pessoa = cursor.fetchall()
    connect.close()
    return pessoa

#UPDATE pessoas (idade, altura, peso)
def atualizar_pessoa(pessoas_id, age=None, height=None, weight=None):
    campos = []
    valores = []

    if age is not None:
        campos.append("age = ?")
        valores.append(age)
    if height is not None:
        campos.append("height = ?")
        valores.append(height)
    if weight is not None:
        campos.append("weight = ?")
        valores.append(weight)

    valores.append(pessoas_id)
    connect = sqlite3.connect('bmi.db')
    connect.cursor().execute(
        f'UPDATE pessoas SET {", ".join(campos)} WHERE pessoas_id = ?',
        valores)
    connect.commit()
    connect.close()

#DELETE pessoas
def excluir_users(pessoas_id):
    connect = sqlite3.connect('bmi.db')
    connect.cursor().execute('DELETE FROM users WHERE pessoas_id= ?', (pessoas_id,))
    connect.commit()
    connect.close()