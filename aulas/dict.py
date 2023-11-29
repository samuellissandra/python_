# Método copy(): retorna uma cópia do dicionário.
dicionario = {"nome": "samuel", "idade": 34, "telefone": "81996584463"}
dicionario_copia = dicionario.copy()
print(dicionario_copia) # Output: {'nome': 'samuel', 'idade': 34}


# Método clear()
dicionario_copia.clear()
print(dicionario_copia) # Output: {}

# Método fromkeys(): cria um novo dicionário com as chaves especificadas e o mesmo valor para todas as chaves

chaves = ["chave1", "chave2", "chave3"]
valor_padrao = 0
dicionario_01 = dict.fromkeys(chaves, valor_padrao)
print(dicionario_01) # Output: {"chave1": 0, "chave2": 0, "chave3": 0}


# Método get()
print(dicionario.get("Sobrenome", "Essa chave não foi encontrada")) # Output: "Essa chave não foi encontrada""
print(dicionario.get("nome")) # Output: "samuel"

# Método items()
print(dicionario.items()) # Output: [('nome', 'samuel'), ('idade', 34)]


# Método keys(): retorna uma lista contendo as chaves do dicionário.
print(dicionario.keys()) # Output: ['nome', 'idade']


# Método pop(): remove e retorna o valor da chave especificada. Se a chave não existir, retorna None (ou um valor especificado como parâmetro).
valor = dicionario.pop("telefone")
print(dicionario) # Output: {'nome': 'samuel', 'idade': 34}
print(valor) # Output: 81996584463


#Adicionar o inter No dicionário
dicionario["cpf"] = "077004894-32"

# Método popitem(): remove e retorna uma tupla contendo a chave e o valor do último item adicionado no dicionário.
item = dicionario.popitem()
print(dicionario) # Output: {'nome': 'samuel', 'idade': 34}
print(item) # Output: ('cpf', '077004894-32')


# Método : retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor padrão 
# (ou um valor especificado como parâmetro) e retorna o valor padrão.setdefault()
print(dicionario.setdefault("casa", "Não existe uma chave como valor casa.")) # Output: Não existe uma chave como valor casa.
#Adicionar o inter No dicionário
dicionario["casa"] = "surubim"
print(dicionario.setdefault("casa", "Não existe uma chave como valor casa.")) # Output: surubim

# Se a chave existir faz o update se a chave não existir é criada uma nova chave.
dicionario.update({"casa": "pernambuco"}) 
# update() também pode ser usado para atualizar um dicionário com argumentos nomeado.
dicionario.update(idade=200) # 
print(dicionario)


# Método values() retorna as chaves.
print(dicionario.values()) # Output: ['samuel', 200, 'pernambuco']


for chave, valor in dicionario.items():
    print(f'A chave --> {chave} tenhe valore --> {valor}')
""" Output:
A chave --> nome tenhe valore --> samuel
A chave --> idade tenhe valore --> 200
A chave --> casa tenhe valore --> pernambuco"""

for chave in dicionario:
    print(chave)
""" Output:
nome
idade
casa
"""

for chave in dicionario:
    print(dicionario[chave])
""" Output:
samuel
200
pernambuco
"""
