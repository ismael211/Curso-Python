print('\033[1;33m##### DESAFIO 43 #####\033[m\n')
peso = float(input("Qual seu peso? {kg} "))
alt = float(input('Qual sua altura? {cm} '))
imc = peso/(alt*alt)
print("O seu IMC é: {:.1f}".format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal!')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está obeso.')
else:
    print('Você tem obesidade morbida.')