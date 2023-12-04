import json

# -*- coding: utf-8 -*-

with open(r'C:\Users\samue\OneDrive\Documentos\GitHub\python_\aulas\resultados.json','r') as arq:
    json_arq = json.load(arq)
    print(json_arq)
