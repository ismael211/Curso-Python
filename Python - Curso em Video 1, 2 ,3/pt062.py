print('\033[1;33m##### DESAFIO 63 #####\033[m\n')
#fibonacci
print('=-'*30)
n = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print('=-'*30)
print('[{}]→[{}]→'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print('[{}]→'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' cabô')