print('\033[1;33m##### DESAFIO 77 #####\033[m\n')
while True:
    word = str(input('\nDigite uma palavra para ver as vogais: '))
    print(f'\nNa palavra {word} temos as vogais: ', end='')    
    for c in word:
        for f in range (len(c)):
            if c[f].lower() in 'aeiou':
                print(f'{c[f]} ', end='')
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('\nDeseja escrever outra palavra? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print('\nObrigado!\n')
