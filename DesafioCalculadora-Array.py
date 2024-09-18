while True:
        print(   " _______________________________\n"
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

        escolha = input("Digite sua opção (1/2/3/4/5/6): ")

        if escolha == '6':
            print("Fim de Código.")
            break

        if escolha == '5':
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            continue
        
        if escolha in ['1', '2', '3', '4']:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"A soma de {numero1} e {numero2} é: {numero1+numero2}")
            elif escolha == '2':
                print(f"A subtração de {numero1} e {numero2} é: {numero1-numero2}")
            elif escolha == '3':
                print(f"A multiplicação de {numero1} e {numero2} é: {numero1*numero2}")
            elif escolha == '4':
                if numero2 != 0:
                    print(f"A divisão de {numero1} e {numero2} é: {numero1/numero2}")
                else:
                    print("Erro: Divisão por zero!")
        else:
            print("Opção inválida. Tente novamente.")