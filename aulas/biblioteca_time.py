"""
OBS:
1_ Biblioteca time:
Oferece funcionalidades básicas para trabalhar com timestamps e estruturas de tempo.
Adequada para tarefas simples que envolvem medições de tempo ou pausas no programa.
Não lida diretamente com fusos horários ou formatação avançada.
Biblioteca datetime:

2_ Biblioteca datetime:
Fornece uma interface mais robusta para trabalhar com datas e horas.
Permite manipulações avançadas, como cálculos entre datas, formatação de strings, parsing e manipulação de fusos horários.
Integra-se bem com a biblioteca pytz para manipulação eficaz de fusos horários.

Recomendação:
Se você precisa realizar manipulações mais avançadas, como cálculos de datas, manipulação de fusos horários, formatação personalizada e parsing de strings de data/hora, a biblioteca datetime é mais adequada. Além disso, a combinação de datetime com pytz é especialmente poderosa quando se lida com fusos horários.

No entanto, se você estiver realizando tarefas mais simples, como medições de tempo, pausas no programa ou operações básicas, a biblioteca time pode ser suficiente e é mais leve.

Em resumo, se o seu projeto envolve manipulações complexas de datas e horas, considere usar a biblioteca datetime em conjunto com pytz. Se a sua aplicação é mais simples e não exige funcionalidades avançadas, a biblioteca time pode ser mais adequada.
"""


import time

# Exemplo de uso de time.time()
timestamp_atual = time.time()
print("Timestamp atual:", timestamp_atual)

# Exemplo de uso de time.sleep()
print("Início do programa")
time.sleep(2)
print("Fim do programa após 2 segundos de pausa")


# Exemplo de uso de time.struct_time
timestamp_atual = time.time()
data_hora = time.localtime(timestamp_atual)
print("Estrutura de data e hora:", data_hora)

# Convertendo para uma string formatada
data_formatada = time.strftime("%Y-%m-%d %H:%M:%S", data_hora)
print("Data formatada:", data_formatada)


data_hora_atual = time.localtime()
data_formatada = time.strftime("%Y-%m-%d %H:%M:%S", data_hora_atual)
print("Data e hora formatadas:", data_formatada)


data_string = "2023-12-20 15:30:00"
data_hora = time.strptime(data_string, "%Y-%m-%d %H:%M:%S")
print("Estrutura de data e hora a partir da string:", data_hora)


data_hora_atual = time.localtime()
timestamp_atual = time.mktime(data_hora_atual)
print("Timestamp atual:", timestamp_atual)


# Obtendo a hora local do sistema
hora_atual_sistema = time.localtime()
# Exibindo a hora atual
"""Neste exemplo, hora_atual.tm_hour, hora_atual.tm_min e hora_atual.tm_sec representam a hora, minutos e segundos, respectivamente. A formatação com :02d garante que os valores sejam exibidos com dois dígitos, adicionando um zero à esquerda, se necessário."""
print(f'Hora atual: {hora_atual_sistema.tm_hour:02d}:{
    hora_atual_sistema.tm_min:02d}:{hora_atual_sistema.tm_sec:02d}')



# Obtendo a hora local do sistema
hora_atual = time.localtime()
# Exibindo a data e a hora atuais
data_hora_atual = time.strftime("%Y-%m-%d %H:%M:%S", hora_atual)
print(f'Data e hora atual: {data_hora_atual}')



from datetime import datetime
import pytz

# Especifica o fuso horário desejado para o Brasil (São Paulo)
fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

# Obtém a hora atual em UTC
hora_utc = datetime.utcnow()

# Converte a hora UTC para o fuso horário do Brasil
hora_fuso_horario_brasil = hora_utc.replace(tzinfo=pytz.utc).astimezone(fuso_horario_brasil)

# Exibe a hora no fuso horário do Brasil
print(f'Hora atual em {fuso_horario_brasil.zone}: {hora_fuso_horario_brasil.strftime("%Y-%m-%d %H:%M:%S %Z")}')



