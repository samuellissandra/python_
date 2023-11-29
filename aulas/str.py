# Exemplo com todos os métodos da classe str
s = "exemplo de string"

# Métodos de formatação
print(s.capitalize())  # Transforma o primeiro caractere em maiúsculo
print(s.casefold())  # Transforma a string em caixa baixa, aplicando todas as regras de maiúsculas e minúsculas
print(s.center(20))  # Centraliza a string em um campo de 20 caracteres
print(s.count("e"))  # Conta o número de ocorrências do caractere ou substring especificados
print(s.encode())  # Retorna uma versão codificada da string em bytes
print(s.endswith("ing"))  # Verifica se a string termina com o sufixo especificado
print(s.expandtabs(tabsize=8))  # Expande os caracteres de tabulação para o número especificado de espaços em branco
print(s.find("e"))  # Retorna a posição da primeira ocorrência da substring especificada
print(s.format())  # Formata a string com os argumentos especificados
print(s.format_map({}))  # Formata a string com um mapeamento de argumentos
print(s.index("e"))  # Retorna a posição da primeira ocorrência da substring especificada. Lança uma exceção se não encontrar

# Métodos de verificação
print(s.isalnum())  # Verifica se a string é alfanumérica (ou seja, consiste apenas de letras e números)
print(s.isalpha())  # Verifica se a string é alfabética (ou seja, consiste apenas de letras)
print(s.isascii())  # Verifica se a string contém apenas caracteres ASCII
print(s.isdecimal())  # Verifica se a string contém apenas dígitos decimais
print(s.isdigit())  # Verifica se a string contém apenas dígitos (incluindo dígitos Unicode)
print(s.isidentifier())  # Verifica se a string é um identificador Python válido
print(s.islower())  # Verifica se a string contém apenas caracteres em caixa baixa
print(s.isnumeric())  # Verifica se a string contém apenas caracteres numéricos
print(s.isprintable())  # Verifica se a string é imprimível (ou seja, não contém caracteres de controle)
print(s.isspace())  # Verifica se a string contém apenas caracteres de espaço em branco
print(s.istitle())  # Verifica se a string segue as regras de capitalização de título (ou seja, cada palavra começa com letra maiúscula)
print(s.isupper())  # Verifica se a string contém apenas caracteres em caixa alta

# Métodos de manipulação
print(s.join(["1", "2", "3"]))  # Concatena os elementos da lista com a string como separador
print(s.ljust(20))  # Alinha a string à esquerda em um campo de 20 caracteres
print(s.lower())  # Converte a string em caixa baixa
print(s.lstrip())  # Remove espaços em branco do início da string
print(s.maketrans({"e": "a"}))  # Cria um objeto de tabela de tradução para substituir caracteres na string
print(s.partition("de"))  # Separa a string em três partes, com a substring especificada como separador
print(s.removeprefix("ex"))  # Remove prefixo "ex" da string
print(s.removesuffix("ing"))  # Remove sufixo "ing" da string
print(s.replace("e", "a"))  # Substitui todas as ocorrências de "e" por "a"
print(s.rfind("e"))  # Retorna a posição da última ocorrência de "e"
print(s.rindex("e"))  # Retorna o índice da última ocorrência de "e"
print(s.rjust(20))  # Centraliza a string em uma largura de 20 caracteres, preenchendo com espaços à esquerda
print(s.rpartition("de"))  # Separa a string em três partes na última ocorrência de "de"
print(s.rsplit(maxsplit=-1))  # Separa a string em uma lista de substrings, a partir da direita
print(s.rstrip())  # Remove espaços em branco do lado direito da string
print(s.split(sep=None, maxsplit=-1))  # Separa a string em uma lista de substrings, usando o separador especificado ou espaço em branco como padrão
print(s.splitlines(keepends=False))  # Separa a string em uma lista de linhas, removendo os caracteres de quebra de linha (\n)
print(s.startswith("ex"))  # Verifica se a string começa com "ex"
print(s.strip())  # Remove espaços em branco do lado esquerdo e direito da string
print(s.swapcase())  # Inverte as letras maiúsculas para minúsculas e vice-versa
print(s.title())  # Transforma a string em título, capitalizando a primeira letra de cada palavra
print(s.translate({}))  # Retorna uma cópia da string com caracteres substituídos de acordo com a tabela de tradução especificada
print(s.upper())  # Converte todos os caracteres da string para maiúsculas
print(s.zfill(20))  # Preenche a string com zeros à esquerda, para uma largura total de 20 caracteres



