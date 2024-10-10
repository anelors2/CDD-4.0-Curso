def lista_unica(lista):    
    return list(set(lista))

a = [10, 12, 12, 31, 4, 4, 5, 31, 6, 7, 6, 8]
nova_lista = lista_unica(a)
print(nova_lista)
