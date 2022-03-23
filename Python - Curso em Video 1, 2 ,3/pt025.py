from random import randint
from time import sleep
print("###### DESAFIO 28 ######\n")
num = 6
while num < 0 or num > 5:
    num = int(input('Digite um numero de 0 a 5: '))
n = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if num == n:
    print(f"Caralho era {n} tu acertou, que sorte!")
else:
    print(f'Você disse {num}, mas o certo era {n}')