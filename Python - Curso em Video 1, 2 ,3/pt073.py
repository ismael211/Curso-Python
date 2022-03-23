print('\033[1;33m##### DESAFIO 73 #####\033[m\n')
#Tabela Laliga
cont = 0
tab = ('Atlético de Madrid', 'Barcelona', 'Real Madrid', 'Sevilla', 'Real Sociedad',
 'Betis', 'Villarreal', 'Granada', 'Athletic Bilbao', 'Levante', 'Celta', 'Valencia',
  'Osasuna', 'Getafe', 'Cádiz', 'Valladolid', 'Elche', 'Eibar', 'Alavés', 'Huesca')
print('''[1] Tabela Completa da LaLiga
[2] Os 4 primeiros Colocados
[3] Os 3 últimos Colocados
[4] Os times em ordem alfabética
[5] Em que posição Barcelona está colocado\n''')
while True:
    esc = int(input('O que deseja ver? Escolha um número de 1 a 5: '))
    if esc < 1 or esc > 5:
        print('Tente novamente. ', end='')
    else:
        break
if esc == 1:
    print(tab)
if esc == 2:
    print(tab[:4])
if esc == 3:
    print(tab[-3:])
if esc == 4:
    print(sorted(tab))
if esc == 5:
    club = str(input('Qual clube você quer ver a colocação? '))
    for p in tab:
        if p == club:
            print(f'O {club} está na {tab.index(club)+1}º posição.')
print('\nEspero que tenha gostado!!!\n')
