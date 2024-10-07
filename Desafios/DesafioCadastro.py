usuario = []
senha = []

while True:
    print(f'____Menu____\n'
        '1 - Cadastro\n'
        '2 - Login\n'
        '3 - Mostrar Usuários\n'
        '4 - Sair\n'
        'Digite sua Opção:')
    escolha = int(input(''))

    if escolha == 4:
        print("Fim do Programa.")
        break
    elif escolha == 3:
        for users in usuario:
            print(f'Usuário: {users}')
    elif escolha == 2:
        nome = input("Digite o login: ")
        senhas = input("Digite a senha: ")        
        for x in range(len(usuario)):
            if usuario[x] == nome and senha[x] == senhas:
                print(f"Bem vindo, {nome}")
                break
    elif escolha == 1:
            nome = input("Digite o login: ")
            senhas = input("Digite a senha: ")
            usuario.append(nome)
            senha.append(senhas)            
    else:
        print(f'Opção invalida.\n'
            ' Tente novamente.')

