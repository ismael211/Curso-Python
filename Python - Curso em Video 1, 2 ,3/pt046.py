print('\033[1;33m##### DESAFIO 48 #####\033[m\n')
#Soma dos numeros impares divisiveis por 3
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'A soma dos {cont} valores é {s}')
