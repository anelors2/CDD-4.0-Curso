num = [0]*10
contador = len(num)

for cont in range(contador):
    num[cont] = int(input('Digite um número: '))

segnum = int(input('Digite outro número: '))
con=0
for x in range(contador):
    if num[x] == segnum:
        con+=1
print(f'{segnum} aparece {con} vezes')
