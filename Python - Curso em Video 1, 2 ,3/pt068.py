print('\033[1;33m##### DESAFIO 69 #####\033[m\n')
cont = contm = contf = 0
while True:
    print('--'*15)
    print('CADASTRE UMA PESSOA')
    print('--'*15)
    ida=int(input("Qual sua idade? "))
    sex=' '
    while sex not in 'FM':
        sex=str(input("Qual seu sexo? [F/M] ")).strip().upper()[0]
    print('--'*15)
    if ida > 18:
        cont += 1
    if sex == 'M':
        contm += 1
    if sex == 'F' and ida < 20:
        contf += 1
    esc=' '
    while esc not in 'SN':
        esc=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if esc=='N':
        break
print(f"A quantidade de pessoas maiores de 18 anos é: {cont}")
print(f"A quantidade de homens cadastrados foi: {contm}")
print(f"A quantidade de mulheres com menos de 20 anos é: {contf}")
