print("###### DESAFIO 34 ######\n")
sal = float(input('Qual seu salario? '))
if sal>=1250.00:
    acres = (sal*0.10)+sal
    print('\033[1;35mSeu novo salario será R${} reais.\033[m'.format(acres))
else:
    acres = (sal*0.15)+sal
    print('\033[1;36mSeu novo salario é R${} reais.\033[m'.format(acres))