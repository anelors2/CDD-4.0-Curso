nomes = ['']*5
senha = ['']*5
contador = len(nomes)

for x in range (contador):
    nomes[x] = input(f'Qual seu nome: ')
    senha[x] = input(f'Qual sua senha {nomes[x]}: ')

for i in range (contador):
    print(f'{i+1} - Cliente {nomes[i]}, sua senha é {senha[i]}')

