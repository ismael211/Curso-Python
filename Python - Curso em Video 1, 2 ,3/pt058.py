from time import sleep
print('\033[1;33m##### DESAFIO 59 #####\033[m\n')
#crie um programa que leia dois valores e veja quais funcionalidades vc quer aplicar
sair = 1
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while sair != 5:
    print('=='*15)
    print('''[1] Para somar
[2] Para multiplicar
[3] Maior e Menor
[4] Digitar os números novamente
[5] Sair do programa\n''')
    esc = int(input(f'O que deseja fazer com {n1} e {n2}?: '))
    if esc == 1:
        print('A soma de {} mais {} é: {}'.format(n1, n2, n1+n2))
        print('-' * 35)
    elif esc == 2:
        print('{} x {} é igual a: {}'.format(n1, n2, n1*n2))
        print('-' * 35)
    elif esc == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
            print('-'*35)
        else:
            print(' O número {} é maior que {}'.format(n2, n1))
            print('-' * 35)
    elif esc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        sair = 1
    elif esc == 5:
        sair = 5
    else:
        print('\033[31mOpção inválida, tente novamente!\033[m')
    sleep(2)
print('Fim do programa! xxx')