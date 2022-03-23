print('\033[1;33m##### DESAFIO 56 #####\033[m\n')
#nome, idade, sexo. Mostrar média de idade, homi mais véi, quantas mulheres < 20
acm = 0
mais = 0
cont = 0
name = ''
for c in range(1, 5):
    print('------ {}º PESSOA -------'.format(c))
    nome = str(input('Qual seu nome? '))
    idad = int(input('Qual sua idade? '))
    sex = str(input('Qual seu sexo? ')).upper()
    acm += idad
    if c == 1 and sex == 'M':
        name = nome
    if idad > mais and sex == 'M':
        name = nome
    if idad < 21 and sex == 'F':
        cont += 1
print('A média de idade é {}'.format(acm/4))
print('O nome do homem mais velho é {}'.format(name))
print('{} mulheres são maiores de idade'.format(cont))