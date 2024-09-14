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
            print(f"Senha incorreta. Você tem mais {chances} tentativa.")
        else:
            print("Você foi bloqueado.")
