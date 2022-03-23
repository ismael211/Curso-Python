from time import sleep
print(f'\033[1;33m{" DESAFIO 98 ":#^30}\033[m')
def contador():
    print('=-'*15)
    print("Contagem de 1 até 10 de 1 em 1: ")
    for c in range(1, 11):
        print(f'{c} ')
    print("FIM!")
    print('=-'*20)


def contador2():
    print("Contagem de 10 até 0 de 2 em 2: ")
    for c in range(10, -1, -2):
        print(f'{c} ')
    print("FIM!")
    print('=-'*20)


def contador3(a, b, c):
    if a > b:
        b = b - 1
        if c > 0:
            c = -c
        elif c == 0:
            c = -1
    print('=-'*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for d in range(a, b, c):
        print(f'{d} ')
        sleep(1)
    print('FIM!')
    print('=-'*20)


contador()
contador2()
print('Agora é sua vez de personalizar a contagem! ')
contador3(a=int(input("Inicio: ")), b=int(input("Fim: ")), c=int(input("Passo: ")))
