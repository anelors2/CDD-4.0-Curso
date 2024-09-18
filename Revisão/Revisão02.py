
repetir = 1

while repetir != 2:

    num1 = float(input('Digite um número: '))

    div = num1 % 2


    if num1 > 0 and div != 0:
        print(f'Numero positivo impar {num1}')
    else:
        if num1 > 0 and div == 0:
            print(f'Numero positivo par {num1}')
        else:
            if num1 < 0 and div != 0:
                print(f'Numero negativo impar {num1}')
            else:
                if num1 < 0 and div == 0:
                    print(f'Numero negativo par {num1}')
                else:
                    print(f"Número {num1} é zerado ou invalido")
    repetir = int(input(("Deseja repetir caga-sangue? \n"
                         "1 - Sim \n"
                         "2 - Não \n")))
    if repetir != 2 or repetir != 1:
        print("Opção invalida burro, sabe ler saporra não?")
        repetir = int(input(("Deseja repetir caga-sangue? \n"
                             "1 - Sim \n"
                             "2 - Não \n")))