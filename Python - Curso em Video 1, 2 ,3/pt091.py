print(f'\033[1;33m{" DESAFIO 89 ":#^30}\033[m\n')
bolet = []
esc = ''
while True:
    nome = str(input('Qual seu nome? '))
    nota = int(input(f'Nota 1: '))
    nota1 = int(input(f'Nota 2: '))
    media = (nota+nota1)/2
    bolet.append([nome, [nota, nota1], media])
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper() 
    if esc == 'N':
        break
print('=-'*15)
print('''\nNº       NOME         MÉDIAS''')
print('--'*15)
for pos, c in enumerate(bolet):
    print(f'{pos:<}{c[0]:^20}{c[2]:>5}', end='')
    print()
print('--'*15)
print('\n\033[31m999 PARA INTERROMPER\033[m\n')
while True:
    num = int(input('Número do aluno para ver as notas: '))
    if num == 999:
        break
    for pos, c in enumerate(bolet):
        if num == pos:
            print(f'As notas do(a) {c[0]} são: {c[1]}')
    print('--'*20)
print('\nVolte sempre! x\n')
