def ListaUnica(lista):
    nova_lista = []
    for x in lista:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

# from DesafioFuncaoListas import *

# l = [10, 12, 12, 31, 4, 4, 5, 31, 6, 7, 6, 8]

# listal = ListaUnica(l)
# print(listal)