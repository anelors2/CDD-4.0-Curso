# Desafio - Faça um código para ler uma senha de usuário
# e após 3 tentativas erradas, sair do programa,
# informando que a senha está bloqueada.


senha = '1234'

chances = 3

while chances > 0:

    codigo = input("Digite a senha: ")
    if codigo == senha:
        print("Senha correta!")
        chances = 0 
    else:
        chances -= 1
        if chances > 0:
            print(f"Senha incorreta. Você tem mais {chances} tentativas.")
        else:
            print("Senha bloqueada.")
