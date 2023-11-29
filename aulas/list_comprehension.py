# Filtrar elementos de uma lista
original_list = [1, 2, 3, 4, 5]
new_list = [2*x for x in original_list]
print(new_list)  # saida: [2, 4, 6, 8, 10]

# Criar uma lista a partir de uma string:
string = "Hello, World!"
letters_list = [char for char in string if char.isalpha()]
# saida: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
print(letters_list)


string = "Abc123"
non_alnum_chars = [char for char in string if not char.isalnum()]
if not non_alnum_chars:
    print("A string é alfanumérica!")
else:
    print("A string não é alfanumérica.")

# Criar uma lista de tuplas:
nomes = ["Alice", "Bob", "Charlie"]
cumprimento_de_nome = [(nome, len(nome)) for nome in nomes]
print(cumprimento_de_nome)  # saida: [('Alice', 5), ('Bob', 3), ('Charlie', 7)]


# Criar uma lista aninhada:
matrix = [[i+j for i in range(3)] for j in range(4)]
print(matrix)  # saida: [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]


# Criar uma lista de dicionários:
alunos = [{"nome": "Alice", "nota": 8}, {"nome": "Bob", "nota": 7}]
nomes = [aluno["nome"] for aluno in alunos]
print(nomes)  # saida: ['Alice', 'Bob']
