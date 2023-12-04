import json

# Não pode criar o arquivo Json.py com o mesmo nome do pacote Json da um erro.

# Abre o arquivo JSON em modo de leitura
with open(r"C:\Users\samue\OneDrive\Documentos\GitHub\python_\aulas\resultados.json", "r") as arq:
    # Carrega o conteúdo do arquivo JSON para a variável 'valor'
    valor = json.load(arq)
    # print(json.dumps(valor, indent=4))  # Imprime os dados com formatação usando json.dumps
    for dados in valor:
        print(dados['dados'])



