from datetime import datetime, timedelta

# Retorna a data e a hora atuais
agora = datetime.now()

data = agora.date()
horario = agora.time()

ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second


data_atual = datetime.now()
data_futura = data_atual + timedelta(days=10)
dez_horas_adiante = data_atual + timedelta(hours=10)


# Diferença entre duas datas
data1 = datetime(2023, 6, 25)
data2 = datetime(2023, 7, 25)

diferenca = data2 - data1
diferenca.days


# ---------------------------------------------------------------
from datetime import date

hoje = date.today()

ano = hoje.year
mes = hoje.month
dia = hoje.day


# ---------------------------------------------------------------
# Criação de um objeto datetime
'''
year, month, day, hour, minute, second, microsecond, tzinfo
'''

data = datetime(2023, 7, 20, 8, 30, 20)

# Converte uma string em um objeto datetime
data_hora_iso = datetime.fromisoformat("2023-06-26 15:30:20")


# ---------------------------------------------------------------
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

agora = datetime.now()
data_formatada = agora.strftime("%A, %d de %B de %Y, %H:%M:%S")

string_data = "30 Junho, 2023, 15:30:20"
formato = "%d %B, %Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)


# ---------------------------------------------------------------
# Trabalhando com FUSO HORÁRIO
from datetime import timezone

fuso_horario = timezone.utc
fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
# Passar para a keyword argument tzinfo=fuso_horario

from zoneinfo import ZoneInfo

fuso_horario_sao_paulo = ZoneInfo("America/Sao_Paulo")

# Conversão entre fusos
data_hora_atual = datetime.now()

fuso_horario_ny = ZoneInfo("America/New_York")
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
