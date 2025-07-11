import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

aniversario = [
    "11/07/2000",
    "22 de Maio de 1991",
    "04/Abr/1995",
    "1995-Outubro-10",
    "12 Julho 1989",
    "16 de Junho de 1987",
    "04/07/1990",
]

formatos = [
    "%d/%m/%Y",
    "%d de %B de %Y",
    "%d/%b/%Y",
    "%Y-%B-%d",
    "%d %B %Y",
    "%d de %B de %Y",
    "%d/%m/%Y",
]
datas_convertidas = []
for i in range(0, len(aniversario)):
    datas = datetime.strptime(aniversario[i], formatos[i])
    datas_convertidas.append(datas)


hoje = datetime.now()
for data in datas_convertidas:
    if data.day == hoje.day and data.month == hoje.month:
        print(hoje.strftime("Hoje, %A %d de %B de %Y, tem aniversário!"))

datas_ordenadas = sorted(datas_convertidas, key=lambda x: (x.month, x.day))
print("Aniversários organizados por ordem de mês e dia:")
for data in datas_ordenadas:
    print(data.strftime("%d de %B"))

