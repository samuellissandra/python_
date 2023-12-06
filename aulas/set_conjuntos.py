# Definindo os conjuntos originais
conjunto = {1, 2, 3, 4, 8, 11, 12, 15, 18, 19, 20, 22, 23, 24, 25, 'samuel'}
con = {1, 2, 10, 13, 17, 18, 19, 20}

# Adicionando o elemento 30 ao conjunto conjunto
conjunto.add(30)


# Copiando o conjunto 'conjunto' para 'copia_conjunto'
copia_conjunto = conjunto.copy()

# Criando um novo conjunto com a diferença entre 'conjunto' e 'con'
diferenca = conjunto.difference(con)

# Atualizando 'conjunto' com a diferença entre 'conjunto' e 'con'
conjunto.difference_update(con)

# Descartando o elemento 8 de 'conjunto'
conjunto.discard(8)

# Criando um novo conjunto com a interseção de 'conjunto' e 'con'
intersecao = conjunto.intersection(con)

# Atualizando 'conjunto' com a interseção de 'conjunto' e 'con'
conjunto.intersection_update(con)

# Verificando se 'conjunto' e 'con' são conjuntos disjuntos
sao_disjuntos = conjunto.isdisjoint(con)

# Verificando se 'con' é um subconjunto de 'conjunto'
is_subconjunto = con.issubset(conjunto)

# Verificando se 'conjunto' é um superconjunto de 'con'
is_superconjunto = conjunto.issuperset(con)

# Removendo e retornando um elemento aleatório de 'conjunto'
elemento_removido = con.pop()
print('O elemento removido', elemento_removido)

# Removendo o elemento 11 de 'conjunto'
conjunto_2 = {1, 2, 3, 4, 8, 11, 12, 15, 18, 19, 20, 22, 23, 24, 25}
# Verificando se o conjunto não está vazio antes de usar pop()
if conjunto:
    conjunto.remove(11)
    print("O elemento 11 foi removido.")
else:
    print("O conjunto está vazio, não é possível usar pop()")
print(conjunto)


# Criando um novo conjunto com a diferença simétrica de 'conjunto' e 'con'
diferenca_simetrica = conjunto.symmetric_difference(con)

# Atualizando 'conjunto' com a diferença simétrica de 'conjunto' e 'con'
conjunto.symmetric_difference_update(con)

# Criando um novo conjunto com a união de 'conjunto' e 'con'
uniao = conjunto.union(con)

# Atualizando 'conjunto' com a união de 'conjunto' e um novo conjunto {30, 35, 40}
conjunto.update({30, 35, 40})

# Limpando o conjunto 'con'
con.clear()
