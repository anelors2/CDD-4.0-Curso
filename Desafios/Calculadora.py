# Desafio Calculadora - Digitar 2 números
# Selecionar opções para as 4 operações básicas
# Adicionar botões para fazer outras contas ou finalizar o código


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

while True:
        escolha = input(
                 " _______________________________\n"
                 "| Selecione a opção:            |\n"
                 "| 1 - Soma                      |\n"
                 "| 2 - Subtração                 |\n"
                 "| 3 - Multiplicação             |\n"
                 "| 4 - Divisão                   |\n"
                 "| 5 - Para digitar outro número |\n"                                 
                 "| 6 - Sair                      |\n"
                 "|_______________________________|\n"
                 ""                                   
                 )

        if escolha == '1':
            print(f"A soma de {numero1} e {numero2} é: {numero1+numero2}")
        elif escolha == '2':
            print(f"A subtração de {numero1} e {numero2} é: {numero1-numero2}")
        elif escolha == '3':
            print(f"A multiplicação de {numero1} e {numero2} é: {numero1*numero2}")
        elif escolha == '4':
            if numero2 != 0 and numero1 != 0:
                print(f"A divisão de {numero1} e {numero2} é: {numero1/numero2}")
            else:
                print("Erro: Divisão por zero!")
        elif escolha == '5':
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        elif escolha == '6':
            print("Fim de Código.")
            break
        else:
            print("Opção inválida. Tente novamente.")