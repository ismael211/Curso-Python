print('\033[1;33m##### DESAFIO 65 #####\033[m\n')
resp = 'S'
acm = cont = med = 0
while resp in 'S':
    num = int(input('Type a number: '))
    acm += num
    cont += 1
    if cont == 1:
        mai = men = num
    else:
        if num > mai:
            mai = num
        if num < men:
            men = num
    resp = 'w'
    while resp not in 'SN':
        resp = str(input('Prosseguiria? [S/N] ')).upper().strip()[0]
med = acm/cont
print(f'A média dos números é: {med}')
print(f'O maior valor é {mai}. O menor é {men}')
