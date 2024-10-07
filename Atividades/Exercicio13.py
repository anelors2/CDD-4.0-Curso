numeros = [0]*5
tamanho = len(numeros)
cont = 0
soma = 0
maior=numeros[0]
menor=numeros[0]
for x in range(tamanho):
    numeros[x] = int(input("Digite um nuúmero: "))

for p in range(tamanho):
    if numeros[p] % 2 == 0 :
        print(f'Número Par: {numeros[p]}')
    if numeros[p] > maior:
        maior = numeros[p]
    if numeros[p] < menor:
        menor = numeros[p]

media = soma/tamanho
for x in range(tamanho):
    if numeros[x]> media:
        cont+=1

print(cont)
print(maior)
print(menor)