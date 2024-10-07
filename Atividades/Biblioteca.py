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

def somar_5_numeros(n1,n2,n3,n4,n5):
    soma = n1+n2+n3+n4+n5
    print(soma)

def soma(*numeros):
    result=0
    for i in numeros:
        result += i
    print(result)

def somar(*numeros):
    t=len(numeros)
    res=0
    for i in range(t):
        res = res + numeros[i]
    print(res)

def Texto(texto):
    cont=0
    for x in texto:
        if x in 'zaqxswcdevfrbgtnhymjukiloçp':
            cont+=1
    print(cont)
    t=len(texto)
    for i in range(t-1,-1,-1):
        print(texto[i], end='')


