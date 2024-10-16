try:
    a=4
    b=0
    divisao = a/b
    print(divisao)
except ZeroDivisionError:
    print("Divisão por zero burro")

try:
    print(x)
except NameError:
    print("Variavel não encontrada.")


try:
    a = []*3

    for i in range(5):
        a[i]=int(input('... : '))

except IndexError:
    print("Por obseqio leia direito?")
except ValueError:
    print("Tipo de Valor Errado")


try:
    a = input('....: ')
    print(a)
except SyntaxError:
    print('Ainda ta errado')

