print("###### DESAFIO 29 ######\n")
vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    mul = (vel - 80) * 7
    print(f'\033[31mVocê foi multado. O valor é de R${mul} reais\033[m')
else:
    print('\033[32mContinue dirigindo com segurança, bom dia!\033[m')