print("###### DESAFIO 31 ######\n")
km = int(input('Qual a distancia da viagem? '))
if km <= 200:
    v = km*0.50
    print('O valor dessa viagem é: R${} reais'.format(v))
else:
    v = km*0.45
    print('O valor da passagem é: R${} reais'.format(v))
