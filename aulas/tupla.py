# Operador in
"""
O operador pode ser usado para verificar se um determinado valor está presente em uma tupla.
Ele retorna se o valor estiver presente e caso contrário.in True False"""
tupla = (1, 2, 3)
esta_presente = 2 in tupla
nao_esta_presente = 4 in tupla

print(esta_presente)  # True
print(nao_esta_presente)  # False


# Método index()
"""
O método pode ser usado para obter o índice da primeira ocorrência de um determinado valor em uma tupla.
Se o valor não estiver presente na tupla, uma exceção é lançada.index() ValueError"""
tupla = (1, 2, 3, 2)
indice = tupla.index(2)
print(indice)  # 1


# Método count()
"""
O método pode ser usado para contar o número de ocorrências de um determinado valor em uma tupla.count()"""
tupla = (1, 2, 3, 2)
contador = tupla.count(2)
print(contador)  # 2


# Descompactação de tupla 
"""É possível "descompactar" uma tupla em variáveis individuais. Por exemplo:"""
tupla = ('samuel', 'elissandra', 2009)
nome_ , nome, ano = tupla
print(nome_)  # samuel
print(nome)  # elissandra
print(ano)  # 2009


# Operador +
"""O operador + pode ser usado para concatenar duas ou mais tuplas em uma única tupla."""
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # (1, 2, 3, 4, 5, 6)


# Operador *
tupla = (1, 2, 3)
tupla_repetida = tupla * 3
print(tupla_repetida)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Função sorted()
"""A função sorted() pode ser usada para classificar os elementos de uma tupla em ordem crescente."""
tupla = (3, 1, 2)
tupla_ordenada = sorted(tupla)
print(tupla_ordenada)  # [1, 2, 3]

# Divertimento
"""A função len() pode ser usada para obter o número de elementos em uma tupla"""
tupla = (1, 2, 3)
tamanho = len(tupla)
print(tamanho)  # 3


# A função enumerate
tupla = (1, 2, 3)
for indice, valor in enumerate(tupla):
    print(indice, valor)

# Saída:
# 0 1
# 1 2
# 2 3

# Método reversed()
"""O método 're pode ser usado para iterar sobre os elementos de uma tupla em ordem reversa."""
tupla = (1, 2, 3)
for valor in reversed(tupla):
    print(valor)

# Saída:
# 3
# 2
# 1


# Função any()
"""A função any() pode ser usada para verificar se há pelo menos um elemento em uma tupla que atenda a uma determinada condição."""
tupla = (1, 2, 3, 4, 5)
tem_par = any(numero % 2 == 0 for numero in tupla)
# Verifica se tenhe números pares ma tupla.
print(tem_par)  # True

# Função all()
tupla = (2, 4, 6, 8, 10)
sao_pares = all(numero % 2 == 0 for numero in tupla)
# Retorna true se todos números for pare.
print(sao_pares)  # True


# Operador 'não
tupla = (1, 2, 3)
nao_tem_4 = 4 not in tupla

print(nao_tem_4)  # True


# Indexação e fatiamento
"""
Tuplas são objetos indexáveis e suportam o fatiamento, assim como listas. O índice do primeiro elemento 
é 0 e o índice do último elemento é -1"""
tupla = (1, 2, 3, 4, 5)
print(tupla[0])  # 1
print(tupla[-1])  # 5
print(tupla[1:3])  # (2, 3)


# Tuplas podem ser usadas como chaves de dicionários
"""
Por serem objetos imutáveis, as tuplas podem ser usadas como chaves de dicionários em Python, diferentemente das listas."""
dicionario = {('a', 'b'): 1, ('c', 'd'): 2}
print(dicionario[('a', 'b')])  # 1


# Conversão de tuplas
"""
Tuplas podem ser convertidas em listas e vice-versa utilizando as funções e .list() tuple()"""
tupla = (1, 2, 3)
lista = list(tupla)
print(lista)  # [1, 2, 3]

nova_tupla = tuple(lista)
print(nova_tupla)  # (1, 2, 3)


# Função zip()
"""A função zip() pode ser usada para combinar elementos de múltiplas tuplas em uma nova tupla de tuplas."""
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_zip = tuple(zip(tupla1, tupla2))

print(tupla_zip)  # ((1, 'a'), (2, 'b'), (3, 'c'))


# Uso de tuplas em funções
"""
Tuplas são frequentemente usadas em funções em Python para retornar múltiplos valores de uma só vez."""
def calcular_mediana(lista):
    ordenada = sorted(lista)
    tamanho = len(ordenada)
    if tamanho % 2 == 0:
        return (ordenada[tamanho//2-1], ordenada[tamanho//2])
    else:
        return (ordenada[tamanho//2],)

mediana = calcular_mediana([5, 3, 1, 4, 2])
print(mediana)  # (3, 4)
