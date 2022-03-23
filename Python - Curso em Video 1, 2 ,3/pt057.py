from random import randint
print('\033[1;33m##### DESAFIO 58 #####\033[m\n')
#melhores o jogo do desafio 28
tent = 1
num = randint(1, 10)
n = int(input('Tente advinhar o número de 1 a 10: '))
while n != num:
    if num > n: 
        n = int(input("Try again, but try a greater number:: "))
        tent += 1
        print('-'*35)
    else:
        n = int(input('Try again, but try a smaller number: '))
        tent += 1
        print('-'*35)
if tent == 1:
    print(f'Parabéns, você acertou de primeira')
else:
    print(f'Parabéns, vocẽ precisou de {tent} tentativas')
    