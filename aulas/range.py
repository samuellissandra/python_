"""
A função range() em Python é utilizada para gerar sequências numéricas de valores inteiros consecutivos,
de forma rápida e eficiente. A sintaxe da função é a seguinte:"""
# range(start, stop[, step])
"""
start (opcional): valor inicial da sequência (por padrão, é 0);
stop: valor final da sequência (não é incluído na sequência);
step (opcional): intervalo entre os valores da sequência (por padrão, é 1)."""

for i in range(5):
    print(i)
# Saída:
# 0
# 1
# 2
# 3
# 4

# Também é possível converter o objeto rangelist():
sequencia = range(1, 6)
lista = list(sequencia)
print(lista)  # [1, 2, 3, 4, 5]


"""
A função range() é muito útil em situações onde é necessário executar uma determinada ação um número 
específico de vezes. Por exemplo:"""
for i in range(3):
    print("Olá!")
# Saída:
# Olá!
# Olá!
# Olá!


"""
Além disso, a função range() é bastante utilizada em conjunto com outras funções, como a 'len() e um zip(), 
para realizar operações em sequências de dados."""
nome = "Maria"
idades = [18, 22, 25, 30, 35]
for i, letra in zip(range(len(nome)), nome):
    print(f"{letra} tem {idades[i]} anos.")
# Saída:
# M tem 18 anos.
# a tem 22 anos.
# r tem 25 anos.
# i tem 30 anos.
# a tem 35 anos.


"""
Por fim, é importante mencionar que a função range() pode ser utilizada para criar sequências de 
valores em ordem decrescente, basta utilizar um valor negativo para o parâmetro 'stepstep:"""
for i in range(5, 0, -1):
    print(i)
# Saída:
# 5
# 4
# 3
# 2
# 1
