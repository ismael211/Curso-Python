print('\033[1;33m##### DESAFIO 82 #####\033[m\n')
l = []
p = []
i = []
while True:
    l.append(int(input('Digite um numero: '))) 
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
for c in l:
    if c % 2 == 0:
        p.append(c)
    else:
        i.append(c)
print(f'A lista completa é: {l}')
print(f'Os números pares são: {p}')
print(f'Os números ímpares são: {i}')