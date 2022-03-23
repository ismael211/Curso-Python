print('\033[1;33m##### DESAFIO 72 #####\033[m\n')
#Mostrar o número por extenso
esc = 'S'
ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
  'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while esc in 'S':
    while True:
        num = int(input("Digite um número entre 0 e 20: "))
        if num < 0 or num > 20:
            num = print('Tente novamente: ', end='')
        else:
            break
    print(f'Você digitou {ext[num]}')
    esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
print('\nAté logo!\n')
