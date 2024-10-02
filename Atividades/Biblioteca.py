def piramide1(num):
    for x in range(1,num+1):
        for i in range(1,x+1):
            print(x, end=(''))
        print()

def piramide2(num):
    for x in range(1, num + 1):
        for i in range(1, x + 1):
            print(i, end='')
        print()

def vogais(texto):
    cont = 0
    for x in texto:
        if x in "aeiouAEIOU":
            cont+=1
    print(cont)