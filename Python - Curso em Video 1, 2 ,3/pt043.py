from random import choice
print('\033[1;33m##### DESAFIO 45 #####\033[m\n')
emp = vit = der = 0
eu='PEDRA'
esc=' '
while True:
    print('='*30)
    if esc == 'N':
        break
    while eu not in 'PEDRA' or 'PAPEL' or 'TESOURA':
        if esc == 'N':
            break
        eu = str(input('Pedra, Papel ou Tesoura? ')).strip().upper()
        lis = ['PEDRA', 'TESOURA', 'PAPEL']
        pc = choice(lis)
        if eu == pc:
            print('\nEmpatou, ambos escolheram {}.\n'.format(pc))
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    emp+=1
                if esc =='N':
                    break
        elif eu == 'PEDRA' and pc == 'TESOURA':
            print('\n\033[1;32mVocê ganhou! Você escolheu {} e o PC {}.\033[m\n'.format(eu, pc))
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    vit+=1
                if esc == 'N':
                    break
        elif eu == 'PAPEL' and pc == 'PEDRA':
            print('\n\033[1;32mVocê ganhou! Você escolheu {} e o PC {}.\033[m\n'.format(eu, pc))
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    vit+=1
                if esc == 'N':
                    break
        elif eu == 'TESOURA' and pc == 'PAPEL':
            print('\n\033[1;32mVocê ganhou! Você escolheu {} e o PC {}.\033[m\n'.format(eu, pc))
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    vit+=1
                if esc == 'N':
                    break
        elif pc == 'PEDRA' and eu == 'TESOURA':
            print('\n\033[1;31mVocê perdeu! Você escolheu {} e o PC {}.\033[m\n'.format(eu, pc))
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    der+=1
                if esc == 'N':
                    break
        elif pc == 'PAPEL' and eu == 'PEDRA':
            print('\n\033[1;31mVocê perdeu! Você escolheu {} e o PC {}.\033[m\n'.format(eu, pc))
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    der+=1
                if esc == 'N':
                    break
        elif pc == 'TESOURA' and eu == 'PAPEL':
            print('\n\033[1;31mVocê perdeu! Você escolheu {} e o PC {}.\033[m\n'.format(eu, pc))
            print('='*30)
            esc=' '
            while esc not in 'SN':
                esc=str(input('Deseja jogar novamente? [S/N] ')).strip().upper()[0]
                if esc == 'S':
                    der+=1
                if esc == 'N':
                    break
print('='*30)
print(f'Você venceu {vit} vezes')
print(f'Você perdeu {der} vezes')
print(f'Empatou {emp} vezes')
print('='*30)