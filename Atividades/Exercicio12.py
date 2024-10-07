numeros = [0]*5
tamanho = len(numeros)
media = 0
maior=0
menor=0
for x in range(tamanho):
    numeros[x] = int(input("Digite um nuúmero: "))

for p in range(tamanho):
    if numeros[p] % 2 == 0 :
        print(f'Número Par: {numeros[p]}')

for l in range(tamanho):
    if numeros[l] > maior:
        maior = numeros[l]
        print(f"Maior: {maior}")

for b in range(tamanho):
    if numeros[b] < menor:
        menor = numeros[l]
        print(f"Menor: {menor}")
#numeros.sort()
#print(f'Menor número: {numeros[0]}, Maior número: {numeros[4]}')

for m in range(tamanho):
    media = numeros[m] + media

mediatotal = media/tamanho

print(F"Média: {mediatotal}")

for p in range(tamanho):
    if numeros[p] > mediatotal:
        print(f"Maiores que a média: {numeros[p]}")


