import re
from collections import Counter


logs = """
2020-05-10 20:42:54,687 | INFO -> O programa foi iniciado
2020-05-11 00:09:52,532 | ERROR -> Erro não esperado
2020-05-11 09:01:10,812 | INFO -> O usuário utilizou o sistema
2020-05-11 19:06:13,609 | INFO -> O usuário utilizou o sistema
2020-05-11 20:46:35,271 | ERROR -> Erro não esperado
2020-05-12 08:14:59,895 | ERROR -> Erro não esperado
2020-05-12 11:33:59,700 | INFO -> O usuário utilizou o sistema
2020-05-13 10:20:14,673 | INFO -> O usuário utilizou o sistema
2020-05-13 16:58:10,298 | WARNING -> O usuário tentou fazer uma operação invalida
2020-05-14 03:55:25,383 | INFO -> O usuário utilizou o sistema
2020-05-15 02:59:29,002 | INFO -> O usuário utilizou o sistema
2020-05-15 08:40:33,776 | ERROR -> Erro não esperado
2020-05-15 13:45:29,089 | WARNING -> O usuário tentou fazer uma operação invalida
"""
padrao = r"(\d{4}-\d{2}-\d{2}) (\d{2}):\d{2}:\d{2},\d{3} \| ERROR"

horras_dos_erros = re.findall(padrao, logs)

horas = [hora for data, hora in horras_dos_erros]

contagem = Counter(horas)

print(f'Total de erros: {len(horas)}\nErros por hora:')
for hora, quantidade in contagem.items():
    print(f"{hora}:00 - {quantidade} erro(s)")

