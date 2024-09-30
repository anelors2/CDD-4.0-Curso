A = [0]*10
M = [0]*10
tamanho = len(A)
for i in range(tamanho):
    A[i]=int(input(f'Número {i+1}: '))

x=int(input(f'Número X: '))

for j in range(tamanho):
    M[j] = x*A[j]


print(f'Os números do vetor M são {M}')