nome = ['']*5
cont = len(nome)

for x in range(cont):
    nome[x] = input('digite seu nome:')
print(nome)
for i in range(cont-1,-1,-1):
    print(nome[i])

