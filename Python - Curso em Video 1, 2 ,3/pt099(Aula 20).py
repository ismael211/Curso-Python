'''
def lin(msg):
    print('-='*30)
    print(msg)
    print('-='*30)


lin('Bagulho')
print()
lin('Vamo zuá')
'''
'''
def soma(a, b):
    print(f'A = {a} e B = {b} ')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(a=int(input('Digite o valor de A: ')), b=int(input('Digite o valor de B: ')))
'''

'''
def cont(*num):
    tam=len(num)
    print(f'Recebi {num} ao todo são {tam} números.')


cont(3, 5, 2)
cont(2)
cont(2, 3, 1, 4, 6)
'''

def som(*num):
    s = 0
    for c in num:
        s += c
    print(f'A soma dos números digitados foram {s}')


som(5, 5, 5)
som(5, 5)
som(5, 5, 5, 5)
