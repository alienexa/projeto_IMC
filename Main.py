import sqlite3
from Pessoas import *
from Users import *

def setup_database():
    cria_tabela_users()
    cria_tabela_pessoas()

def register_user():
    print('\nBem vindo ao Registo de utilizadores!')
    print('Por favor indique as informações abaixo ')

    username=input('\nDigite o seu Username: ')
    password=input('Digite a sua Password: ')
    name=input('Digite o seu Nome: ')

    regista_user(username, password, name)
    print(f'{name} registada!')

def login_user():
    print('\nBem vindo ao Login de utilizadores!')
    print('Por favor indique as informações abaixo ')
    username = input('\nDigite o seu Username: ')
    password = input('Digite a sua Password: ')
    if valida_user(username, password):
        user=ler_user(username)
        print(f'\nBem vindo {user[0][3]}')
        return user[0][0]
    else:
        print('As informações inseridas não estão corretas!')

def register_pessoa(user_id):
    print('\nBem vindo ao Registo de Pessoas!')
    print('Por favor indique as informações abaixo ')

    first_name = input('\nDigite o Primeiro Nome: ')
    last_name = input('Digite o Ultimo Nome: ')
    age = input('Digite a Idade: ')
    height = input('Digite a Altura (em metros): ')
    weight = input('Digite o Peso (em quilos): ')

    regista_pessoa(first_name, last_name, age, height, weight, user_id)

def search_pessoas(user_id):
    print('\nPesquisa por pessoa!' )
    search_name = input('Indique o nome da pessoa: ')
    pessoas = ler_pessoas_por_nome(user_id, search_name)

    if pessoas:
        for pessoa in pessoas:
            bmi = calculate_bmi(pessoa[4],pessoa[5])
            print(f"{pessoa[1]} {pessoa[2]} - IMC: {bmi:.2f}")
    else:
        print(f'{search_name} não encontrado! \nPor favor registe {search_name}')

def update_pessoa():
    atualizar_pessoa()

def calculate_bmi(height, weight):
    return weight/height**2

#MAIN
def main():
    setup_database()
    print("Bem-vindo!")
    while True:
        print("\n1. Registrar\n2. Login\n3. Sair")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
            if user_id:
                while True:
                    print("\n1. Adicionar Registro\n2. Buscar\n3. Sair")
                    sub_choice = input("Escolha uma opção: ")
                    if sub_choice == '1':
                        register_pessoa(user_id)
                    elif sub_choice == '2':
                        search_pessoas(user_id)
                    elif sub_choice == '3':
                        break
        elif choice == '3':
            print("Saindo...")
            break

if __name__ == "__main__":
   main()
