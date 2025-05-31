 #Feito por Felipe da Veiga Gomes e Rogerio de Abreu Mar
import json
import hashlib
import itertools
import time

def LerDadosUser():
    with open('usuarios.json') as file:
        data = json.load(file)
        return data

def cadastrar():
    user = input("Digite seu nome:")
    senha = input("Digite sua senha:")
    
    senha_bytes = senha.encode()
    senha_hash = hashlib.sha256(senha_bytes)   
    senha_hash_hex = senha_hash.hexdigest()
    usuarios = {
        "user": user,
        "senha":senha_hash_hex
    }
    dadosUser = LerDadosUser()
    for user_cadastro in dadosUser:
     if user == user_cadastro["user"]:
        print("Usuário já cadastrado")
        return
    dadosUser.append(usuarios)
    
    json_string = json.dumps(dadosUser, indent=4)
    with open('usuarios.json', 'w') as arquivo:
        arquivo.write(json_string)

    print("Cadastro Concluido")

def login(user_login,senha_login):
    user_login = input("Digite seu nome:")
    senha_login = input("Digite sua senha:")

    senha_login = senha_login.encode()
    senha_login_hash = hashlib.sha256(senha_login)
    senha_login_hash_hex = senha_login_hash.hexdigest()

    usuarios = LerDadosUser()

    achou_user = False
    achou_senha = False
    for user in usuarios:
        user_registrado = user["user"]
        senha_registrada = user["senha"]

        if user_registrado == user_login:
            if senha_registrada == senha_login_hash_hex:
                achou_user = True
                achou_senha = True


    if achou_senha and achou_user:
        print("Seja bem vindo", user_login)    
    else:
        print("Nome ou Senha incorretos")                        

def Secao1():         
    opcao = 0
    while opcao != "3":
        opcao = input(" 1 - Cadastro | 2 - Login | 3 - Sair:")
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            user_login = input("Digite seu nome:")
            senha_login = input("Digite sua senha:")
            login(user_login, senha_login)
        elif opcao == "3":
            print("Saindo do sistema...")
        else:
            print("Opção inválida")

def Secao2():
    print("sessao 2")
    inicio_timer_total = time.time()
    dados_usuarios  = LerDadosUser()
    
    for user in dados_usuarios:
        print(f"Procurando senha do usuário: {user['user']}")
        inicio_timer_user = time.time()
        caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
        combinacoes = itertools.product(caracteres, repeat=4) # gerando combinações de 4 caracteres com plano cartesiano
        for combinacao_tupla in combinacoes:
                combinacao = ("".join(combinacao_tupla))#como as combinações são tuplas(plano cartesiano), foi utilizado o join para transformar em string
                combinacao_hash = hashlib.sha256(combinacao.encode())
                combinacao_hash_hex = combinacao_hash.hexdigest()
                if user["senha"] == combinacao_hash_hex:
                    fim_timer_user = time.time()
                    print(f" - Usuario:{user['user']} Senha encontrada: {combinacao}")
                    print(f" - Tempo de execução: {fim_timer_user - inicio_timer_user:.4f} segundos")
                    break
        
    fim_timer_total = time.time()
    print(f"Tempo total de execução: {fim_timer_total - inicio_timer_total:.4f} segundos")
            

opcao = 0
while opcao != "0":
    opcao = input(" Seção 1 - 1 | Seção 2 - 2 | 0 - Sair:")
    if opcao == "1":
        Secao1()
    elif opcao == "2":
        Secao2()
    elif opcao == "0":
        print("Saindo do sistema...")
    else:
        print("Opção inválida")




