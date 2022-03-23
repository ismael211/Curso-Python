print('\033[1;33m##### DESAFIO 36 #####\033[m\n')
val = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salario? '))
anos = int(input('Em quantos anos pretende pagar? '))
prest = (val/anos)/12
sal = sal*0.3
print(f"Para pagar uma casa no valor de {val} em {anos} anos, a prestação custará {prest} por mês")
if sal >= prest:
    print('Vai ser ótimo fazer negocio com você!')
else:
    print('Desculpa, mas não podemos seguir adiante.')