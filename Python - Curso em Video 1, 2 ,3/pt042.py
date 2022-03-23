print('\033[1;33m##### DESAFIO 44 #####\033[m\n')
val = float(input('Qual o valor da compra? '))
print('''\nCOMO DESEJA PAGAR?
[ 1 ] A vista dinheiro ou cheque
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opç = int(input('\nEscolha de 1 a 4: '))
if opç == 1:
    tot = val - (val*0.10)
elif opç == 2:
    tot = val - (val*0.05)
elif opç == 3:
    parcela = val/2
    tot = val
    print('Serão duas parcelas de {:.2f}'.format(parcela))
elif opç == 4:
    parcela = int(input('Quantas parcelas? '))
    tot = val + (val*0.20)
    totpa = tot/parcela
    print('Serão {} parcelas de R${:.2f}'.format(parcela, totpa))
else:
    tot = val
    print('Opção INVÁLIDA tente nomente!')
print('Sua compra de R${:.2f} custará R${:.2f} reais'.format(val, tot))