print('\033[1;33m##### DESAFIO 57 #####\033[m\n')
#PROGRAMA Q LEIA SOMENTE M OU F
M = 'M'
F = 'F'
l = 'ç'
while l not in 'MF':
    l = str(input('Qual seu sexo? (F/M) ')).upper()
if l == M:
    print('Seu sexo é Masculino')
else:
    print('Seu sexo é Feminino')