 #Feito por Felipe da Veiga Gomes e Rogerio de Abreu Mar
import json
import hashlib

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

def login():
    user_login = input("Digite seu nome:")
    senha_login = input("Digite sua senha:")

    usuarios = LerDadosUser()

    achou_user = False
    achou_senha = False
    for user in usuarios:
        user_registrado = user["user"]
        senha_registrada = user["senha"]

        if user_registrado == user_login:
            if senha_registrada == senha_login:
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
            login()
        elif opcao == "3":
            print("Saindo do sistema...")
        else:
            print("Opção inválida")

def Secao2():
    print("sessao 2")
    usuarios  = LerDadosUser()
    for user in usuarios:
        print(user["senha"])



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




