import time

# Retorna o tempo atual em segundos desde a Epoch (1º de janeiro de 1970)
time.time()


tempo_atual_nanosegundos = time.time_ns()

# Faz o programa esperar pelo número de segundos especificado
time.sleep(5)

# Converte um tempo expresso em segundos desde a epoch em uma string representando o tempo local
tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
# Saída: Wed Jun 28 11:45:55 2023


# Converte um tempo expresso em segundos desde a epoch em um objeto struct_time. Este objeto contém
# informações sobre o tempo local, como ano, mês, dia, hora, minuto, segundo. Usa o fuso horário local
time.localtime()


# Converte um objeto de tempo struct para uma string de acordo com um formato específico
tempo_em_struct = time.localtime()
print(time.strftime("%d %B %Y", tempo_em_struct))
print(time.strftime("%H:%M:%S", tempo_em_struct))


# Definir a localização para português
import locale 

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


# Analisa uma string representando um horário de acordo com um formato. O retorno é um objeto struct_time
string_tempo = "30 Junho, 2023"
formato = "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo, formato)

print(f"Tempo em struct: {tempo_em_struct}")


# Converte um objeto struct_time em segundos desde a epoch. Este é o inverso da função localtime() 
tempo_atual = time.localtime()
tempo_ano_novo = time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0))

diferenca = time.mktime(tempo_atual) - tempo_ano_novo


