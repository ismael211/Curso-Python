print('\033[1;33m##### DESAFIO 55 #####\033[m\n')
#Mais pesado e mais leve
maior = 0
menor = 0
for c in range(1, 6):
    print(f'------- {c}º PESSOA --------')
    peso = float(input('Qual seu peso? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'A pessoa com maior peso tem {maior}kg')
print(f'A pessoa mais leve pesa {menor}kg')
