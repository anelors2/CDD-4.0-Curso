nota = [0.0]*5
tamanho = len(nota)
cont = 0
soma = 0
for a in range(tamanho):
    nota[a]=float(input(f'Digite a nota do aluno {a+1}: '))

for i in range(tamanho):
    soma += nota[i]
media = soma / tamanho

for y in range(tamanho):
    if nota[y]>media:
        cont = cont+1

print(f"media é {media} e {cont} alunos tem notas acima da média.")

