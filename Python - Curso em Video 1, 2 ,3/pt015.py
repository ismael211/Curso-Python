import random
print('######### DESAFIO 20 #########\n')
a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de outro aluno: '))
a3 = str(input('Digite o nome de outro aluno: '))
a4 = str(input('Digite o nome de outro aluno: '))
print('~~'*15)
li = [a1, a2, a3, a4]
random.shuffle(li)
print(f'A nova ordem é: {li}')
