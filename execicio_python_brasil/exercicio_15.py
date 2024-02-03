# Solicitando o tamanho do arquivo em MB e a velocidade da internet em Mbps
tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet = float(input("Digite a velocidade da sua internet em Mbps: "))

# Convertendo o tamanho do arquivo para bits e a velocidade da internet para bytes por segundo
tamanho_bits = tamanho_arquivo * 1024 * 1024 * 8
velocidade_bytes = velocidade_internet * 1024 * 1024 / 8

# Calculando o tempo aproximado de download em minutos
tempo_download = tamanho_bits / velocidade_bytes / 60

# Exibindo o resultado
print(f"O tempo aproximado de download é de {tempo_download:.2f} minutos.")
