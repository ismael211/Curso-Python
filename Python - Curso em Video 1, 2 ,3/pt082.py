print('\033[1;33m##### DESAFIO 81 #####\033[m\n')
esc = ''
l = []
while True:
    l.append(int(input('Digite um valor: ')))
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print(f'\nVocê digitou {len(l)} elementos')
l.sort(reverse=True)
print(f'Os números foram: {l}')
if 5 in l: print('Tem o número 5 na lista')
else: print('Não tem 5 na lista\n')
