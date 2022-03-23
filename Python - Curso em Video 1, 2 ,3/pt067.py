from random import randint
print('\033[1;33m##### DESAFIO 68 #####\033[m\n')
#impar ou par
cont = 0
esc = ''
print("=-"*15)
print("VAMOS JOGAR IMPAR OU PAR")
print("=-"*15)
while True:
    esc = 'W'
    while esc not in 'IP':
        esc = str(input("Você quer impar ou par [I/P]? ")).strip().upper()[0]
    n = int(input("Escolha um número: "))
    print('--'*15)
    pc = randint(1,10)
    som = n+pc
    if esc == 'P':
        if som%2 == 0:
            print(f"Você jogou {n} e o Computador {pc}. Total foi {som} DEU PAR")
            print('--'*15)
            print("VOCÊ VENCEU!")
            print("Let's play again...")
            cont += 1
        else:
            print(f"Você jogou {n} e o Computador {pc}. Total foi {som} DEU IMPAR")
            print('--'*15)
            print('VOCÊ PERDEU!')
            break
    if esc == 'I':
        if som%2 == 0:
            print(f"Você jogou {n} e o Computador {pc}. Total foi {som} DEU PAR")
            print('--'*15)
            print("VOCÊ PERDEU!")
            break
        else:
            print(f"Você jogou {n} e o Computador {pc}. Total foi {som} DEU IMPAR")
            print('--'*15)
            print('VOCÊ VENCEU!')
            print("Let's play again...")
            cont += 1
print(f'GAME OVER! Você venceu um total de {cont} vezes.')
