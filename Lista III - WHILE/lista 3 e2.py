while True:
    login = str (input('Usuário: '))
    senha = str (input('senha: '))
    if login == senha:
        print ('usuário e senha não podem ser iguais')
    else:
        print (f' Bem vindo, {login}')
        break
