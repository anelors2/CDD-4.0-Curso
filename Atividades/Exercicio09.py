login = ['']
senha = ['']
login_correto = ['']
senha_correta = ['']
opcao = 0
while opcao != 4:
    print('Menu\n'
          '1 - Cadastrar\n'
          '2 - Login\n'
          '3 - Mostrar Usuários\n'
          '4 - Sair')
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
    elif opcao == 2:
        login_correto = input("Usuário: ")
        senha_correta = input("Senha: ")
        if login_correto == login and senha_correta == senha:
            print("login Efetuado com sucesso.")
        else:
            print("Login incorreto.")
    elif opcao == 3:
        print(f"Os usuários cadastrados são: {login}")
    elif opcao == 4:
        print("Fim.")

    else:
        print("Opção Invalida. Tente novamente.")

print(login, senha)