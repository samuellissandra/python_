# Aqui estão exemplos de alguns dos métodos mais comuns das listas em Python:

# O método append()
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]


# Método extend()
""" O método extend() é usado para adicionar múltiplos elementos ao final da lista. 
Ele recebe um iterável como argumento e adiciona cada elemento individualmente à lista. Por exemplo"""
lista.extend([5, 6])
print(lista)  # [1, 2, 3, 4, 5, 6]


# Método inserir()
"""
O método insert() é usado para inserir um elemento em uma posição específica da lista. Ele recebe dois argumentos:
o índice onde o elemento será inserido e o próprio elemento. Por exemplo:"""
lista.insert(0, 0) # Foi inserido o zero na posição zero
lista.insert(len(lista), 'samuel') # Foi inserido na última posição usando a função len() o nome "Samuel"
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 'samuel']

# Método remover()
lista.remove("samuel")
print(lista)  # [0, 1, 2, 3, 4, 5, 6]


# Método pop()
"""
O método 'pop é usado para remover o elemento em uma posição específica da lista e retorná-lo. Se nenhum índice for especificado,
o último elemento da lista será removido. Por exemplo:"""
lista_2 = ['samuel', 'elissandra', 'maryanna']
ultimo_elemento = lista_2.pop()
print('Quem ficou na lista', lista_2)  # Quem ficou na lista ['samuel', 'elissandra']
print('Foi removido da lista', ultimo_elemento)  # Foi removido da lista maryanna

segundo_elemento = lista_2.pop(0)
print('Quem ficou na lista', lista_2)  # Quem ficou na lista ['elissandra']
print('Foi removido da lista', segundo_elemento)  # Foi removido da lista samuel


# Método sort()
numero = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numero.sort()
print(numero)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Método reverse()
Modifica = [1, 2, 3]
Modifica.reverse()
print(Modifica)  # [3, 2, 1]


# Método index()
"""
O método 'index é usado para obter o índice da primeira ocorrência de um determinado valor na lista. 
Se o valor não estiver presente na lista, uma exceção 'ValueError é lançada. Por exemplo:"""
lista_03 = [1, 2, 3, 2]
indice = lista_03.index(2)
print(indice)  # 1

# Método count()
lista_04 = [1, 2, 3, 2, 2.3, 23, 2]
contador = lista_04.count(2)
print(contador)  # 3

# Método clear()
lista_04 = [1, 2, 3]
lista_04.clear()
print(lista_04)  # []



# Método copy()
"""
O método 'copy é usado para criar uma cópia superficial da lista. Ou seja, ele cria uma nova lista com os 
mesmos elementos da lista original, mas os elementos em si não são copiados. Por exemplo:"""
lista1 = [1, 2, 3]
lista2 = lista1.copy()

lista1[0] = 4
print(lista1)  # [4, 2, 3]
print(lista2)  # [1, 2, 3]


# Operador in
"""
O operador 'in é usado para verificar se um determinado valor está presente na lista. Ele retorna 'True' 
se o valor estiver presente e 'False' caso contrário. Por exemplo:"""
lista_in = [1, 2, 3]
esta_presente = 2 in lista_in
nao_esta_presente = 4 in lista_in

print(esta_presente)  # True
print(nao_esta_presente)  # False

lista = [1, 2, 3]
lista.append(4) # adiciona 4 no final da lista
lista.extend([5, 6]) # adiciona 5 e 6 no final da lista
lista.insert(0, 0) # insere 0 na posição 0 (início) da lista
lista.remove(3) # remove o primeiro 3 da lista
lista.pop() # remove e retorna o último elemento da lista (6)
lista.index(2) # retorna o índice do primeiro 2 na lista (1)
lista.count(1) # retorna o número de vezes que 1 aparece na lista (1)
lista.sort(reverse=True) # ordena a lista em ordem decrescente
lista.reverse() # inverte a ordem dos elementos da lista
