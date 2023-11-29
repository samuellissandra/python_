# Contador: o while pode ser utilizado para contar até um determinado número:
contador = 0
while contador < 10:
    print(contador)
    contador += 1

"""
Loop infinito: o while pode ser utilizado para criar um loop infinito que só para quando uma determinada 
condição é atingida:"""
while True:
    resposta = 'sair' # input("Digite 'sair' para encerrar o programa: ")
    if resposta == "sair":
        break


""" 
Busca em uma lista: o while pode ser utilizado para buscar um determinado elemento em uma lista:"""
lista = [1, 3, 5, 7, 9]
busca = 5
indice = 0
while indice < len(lista):
    if lista[indice] == busca:
        print(f"O elemento {busca} foi encontrado no índice {indice}.")
        break
    indice += 1
else:
    print(f"O elemento {busca} não foi encontrado na lista.")


def jogo():
    """Jogo de adivinhação: o while pode ser utilizado para criar um jogo de adivinhação onde o usuário tenta
    adivinhar um número aleatório:"""
    import random

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        if palpite == numero_secreto:
            print(f"Parabéns, você acertou o número secreto em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")

# jogo()


def entrada_user():
    """Validando entrada de usuário: o 'while"""
    while True:
        data = input("Digite uma data no formato dd/mm/aaaa: ")
        partes = data.split("/")
        print(partes)
        if len(partes) != 3:
            print("Data inválida. Tente novamente.")
            continue
        try:
            dia = int(partes[0])
            mes = int(partes[1])
            ano = int(partes[2])
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 1900):
                print("Data inválida. Tente novamente.")
                continue
            break
        except ValueError:
            print("Data inválida. Tente novamente.")

entrada_user()