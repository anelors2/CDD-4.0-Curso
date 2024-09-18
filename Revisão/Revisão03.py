# Faça um algoritimo que leia dois valores inteiros A e B,
# se os valores de A e B forem iguais, deverá somar os dois valores,
# caso contrário deverá multiplicar A por B. Ao final de qualquer
# um dos cálculos deve-se atribuir o resultado a uma variável C e
# imprimir  o valor na tela.

num1 = int(input('Digite o valor de A: '))
num2 = int(input('Digite o valor de B: '))

if num1 != num2:
    print(f"A multiplicação de {num1}*{num2}={num1*num2}")
    C = num1*num2
else:
    print(f"A soma de {num1}+{num2}={num1+num2}")
    C = num1+num2

print(f"O valor de C é {C}")