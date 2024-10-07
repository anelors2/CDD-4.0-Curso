lista = [1, 2, 3]
lista.append(4)  # [1, 2, 3, 4] Adiciona um item ao final da lista.


lista = [1, 2, 3]
lista.insert(1, 'a')  # [1, 'a', 2, 3] Insere um item em uma posição específica.


lista = [1, 2, 3]
lista.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]  Adiciona todos os itens de um iterável ao final da lista.


lista = [1, 2, 3, 4]
lista.remove(3)  # [1, 2, 4] Remove a primeira ocorrência de um item na lista.


lista = [1, 2, 3]
lista.pop()  # Retorna 3, lista fica [1, 2] Remove e retorna o item de uma posição específica (por padrão, remove o último).


lista = [1, 2, 3]
lista.clear()  # [] Remove todos os itens da lista, deixando-a vazia.


lista = [1, 2, 3, 2]
lista.index(2)  # Retorna 1 - Retorna o índice da primeira ocorrência de um valor.


lista = [1, 2, 2, 3, 2]
lista.count(2)  # Retorna 3 - Conta quantas vezes um item aparece na lista.


lista = [3, 1, 2]
lista.sort()  # [1, 2, 3] - Ordena os itens da lista.


lista = [1, 2, 3]
lista.reverse()  # [3, 2, 1] -  Inverte a ordem dos itens na lista.


lista = [1, 2, 3]
nova_lista = lista.copy()  # nova_lista = [1, 2, 3] - Retorna uma cópia superficial da lista.




