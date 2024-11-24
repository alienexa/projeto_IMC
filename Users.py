import sqlite3
from operator import truediv


# Criação da tabela de USERS
def cria_tabela_users():
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        name TEXT
                        )
                    ''')
    connect.commit()
    connect.close()

#Operações CRUD para USERS: CREATE users | READ users | UPDATE users | DELETE users

#CREATE users
def regista_user(username, password, name):
    connect = sqlite3.connect('bmi.db')
    connect.cursor().execute(
        'INSERT INTO users (username, password, name) VALUES (?, ?, ?)',
        (username, password, name))
    connect.commit()
    connect.close()

#READ users
def ler_users():
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    connect.close()
    return users

def ler_user(username):
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?',(username,))
    user = cursor.fetchall()
    connect.close()
    return user

#UPDATE users
    #Tratando-se de users não existe a necessidade de atualizar, pelo menos para já.

#DELETE users
def excluir_users(user_id):
    connect = sqlite3.connect('bmi.db')
    connect.cursor().execute('DELETE FROM users WHERE user_id= ?', (user_id,))
    connect.commit()
    connect.close()


#Validar a existencia de users
def valida_user(username, password):
    #Só devolve True or False
    connect = sqlite3.connect('bmi.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?',(username,password))
    user = cursor.fetchall()
    connect.close()

    if user:
        return True
    else:
        return False