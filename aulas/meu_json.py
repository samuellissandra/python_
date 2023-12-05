


import json

cont = 0
meus = {1, 2, 3, 4}
novo = {}

# Abre o arquivo JSON em modo de leitura
with open(r"C:\Users\samue\OneDrive\Documentos\GitHub\python_\aulas\resultados.json", "r") as arq:
    # Carrega o conteúdo do arquivo JSON para a variável 'valor'
    arquivo = json.load(arq)
    
    for dados in arquivo:
        for num in dados['dados']:
            novo = int(num)
            meus.add(novo)
            cont += 1
        
print(cont)
