print("###### DESAFIO 32 ######\n")
from datetime import date
ano = int(input('Qual ano você quer verificar? 0 para ver o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f'{ano} é um ano bissexto')
else:
    print(f'{ano} NÃO é um ano bissexto.')