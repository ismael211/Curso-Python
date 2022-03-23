from datetime import date
print('\033[1;33m##### DESAFIO 39 #####\033[m\n')
ano = date.today().year
sex = str(input('Qual seu sexo? [F/M]: ')).strip().upper()
if sex == 'M':
    nasc = int(input('Qual seu ano de nascimento? '))
    idad = ano - nasc
    print(f"Você nasceu em {nasc}")
    print(f'Quem nasceu em {nasc} tem {idad} anos')
    if idad < 18:
        dif = nasc + 18
        print(f'Você deverá se alistar em {dif}.')
    elif idad == 18:
        print('Já é hora de se alistar.')
    else:
        dif = nasc + 18
        print(f'Seu alistamento foi em {dif}')
else:
    print("Você não precisa se alistar.")
