import csv

def conferi_resultados():
    # Números que queremos verificar se estão presentes em cada linha
    meus_numeros = {
        'bola 1': '1',
        'bola 2': '2',
        'bola 3': '3',
        'bola 4': '4',
        'bola 5': '8',
        'bola 6': '11',
        'bola 7': '12',
        'bola 8': '15',
        'bola 9': '18',
        'bola 10': '19',
        'bola 11': '20',
        'bola 12': '22',
        'bola 13': '23',
        'bola 14': '24',
        'bola 15': '25'
    }

    # Abre o arquivo CSV para leitura
    with open(r"C:\Users\samue\OneDrive\Documentos\GitHub\python_\aulas\loto.csv") as arquivo:
        # Cria um leitor de dicionário para ler o arquivo CSV
        leitura = csv.DictReader(arquivo)

        # Itera sobre cada linha do arquivo CSV
        for linha in leitura:
            # Obtém um conjunto dos números presentes na linha atual
            numeros_na_linha = set(linha.values())

            # Encontra a interseção entre os números desejados e os números na linha
            numeros_encontrados = set(meus_numeros.values()) & numeros_na_linha

            # Se houver pelo menos um número encontrado, imprime a informação
            if numeros_encontrados:
                print(f'{linha["Data"]} - {linha["Concurso"]}: {numeros_encontrados} Acertos = {len(numeros_encontrados)}')


conferi_resultados()