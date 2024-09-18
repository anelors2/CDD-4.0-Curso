# Receber 3 números e comparar se a soma do número 1 e número 2 com o número 3.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite o terceiro número: '))

soma = num1+num2

if soma>num3:
    print(f"A soma de {num1} e {num2} é {soma}.\n"
          f"E {soma} é maior que {num3}")
else:
    if soma==num3:
        print(f'Os números são iguais')
    else:
        print(f"{num3} é maior que {soma}")
