# Exemplo com o laço for em Python

# percorrendo uma lista
lista = [1, 2, 3, 4, 5]
for numero in lista:
    print(numero)

# percorrendo uma string
texto = "Python é uma linguagem de programação"
for letra in texto:
    print(letra)

# percorrendo um objeto range
for i in range(3):
    print("Olá!")

# percorrendo uma lista com índice e valor
lista_frutas = ["maçã", "banana", "laranja"]
for i, fruta in enumerate(lista_frutas):
    print(f"{i}: {fruta}")

# utilizando o if dentro do laço for
for numero in lista:
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")


# Exemplos com listas
frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
    print(fruta)

numeros = [1, 2, 3, 4, 5]
soma = 0
for numero in numeros:
    soma += numero
print(soma)

# Exemplos com tuplas
pares = (2, 4, 6, 8, 10)
for numero in pares:
    print(numero)

# Exemplos com dicionários
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa:
    valor = pessoa[chave]
    print(f"{chave}: {valor}")

notas = {"João": 8.5, "Maria": 9.0, "José": 7.0}
for chave, valor in notas.items():
    print(f"{chave}: {valor}")

# Percorrendo um dicionário e verificando se algum valor é igual a um determinado número:
notas = {"João": 8.5, "Maria": 9.0, "José": 7.0}
tem_nota_maior_que_oito = False
for valor in notas.values():
    if valor > 8:
        tem_nota_maior_que_oito = True
        break

if tem_nota_maior_que_oito:
    print("Pelo menos uma nota é maior do que 8.")
else:
    print("Nenhuma nota é maior do que 8.")

# Verificando se uma chave específica existe no dicionário:
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
if "nome" in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# Percorrendo um dicionário e imprimindo apenas os valores:
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for valor in pessoa.values():
    print(valor)

# Percorrendo um dicionário e imprimindo apenas as chaves:
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa:
    print(chave)

# Percorrendo um dicionário e imprimindo as chaves e valores:
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
for chave in pessoa:
    valor = pessoa[chave]
    print(f"{chave}: {valor}")

