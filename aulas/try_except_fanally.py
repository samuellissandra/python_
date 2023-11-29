# Tentativa de abrir um arquivo
try:
    with open("exemplo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
# Lidando com exceção de arquivo não encontrado
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
# Executando código independente do resultado
finally:
    print("O arquivo foi fechado.")


numeros = [10, 20, 30, 40, 50]
# Solicita ao usuário para fornecer o divisor
divisor = 0  # int(input("Digite um número para ser usado como divisor: "))

try:
    for numero in numeros:
        resultado = numero / divisor
        print(f"{numero} dividido por {divisor} é igual a {resultado}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
finally:
    print("Processamento concluído.")


numeros = [10, 20, 30, 40, 50]

# Solicita ao usuário para fornecer o divisor
while True:
    try:
        # int(input("Digite um número para ser usado como divisor: "))
        divisor = 0
        break
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número inteiro.")

try:
    for numero in numeros:
        resultado = numero / divisor
        print(f"{numero} dividido por {divisor} é igual a {resultado}")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
finally:
    print("Processamento concluído.")


while True:
    try:
        nome = str(input("Digite seu nome: "))
        if nome.isnumeric():
            raise ValueError
        """Não exemplo anterior, usamos 'raise ValueError se o nome fornecido pelo usuário for um número. 
        Quando a exceção é gerada, ela é propagada para o bloco 'exceptexcept correspondente, 
        que exibe uma mensagem de erro e solicita ao usuário que forneça outra entrada válida. 
        Sem o 'raise, o código simplesmente armazenaria o número fornecido pelo usuário como uma string
        na variável 'nomenome, o que não seria a intenção do programa."""
        break
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um nome.")

print(f"Olá, {nome}!")
