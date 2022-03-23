print('\033[1;33m##### DESAFIO 79 #####\033[m\n')
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não adcionado.')
    else:
        lista.append(n)
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
lista.sort()
print(f'Os valores digitados foram: {lista}')
