print('\033[1;33m##### DESAFIO 70 #####\033[m\n')
som = prod = mprec = cont = 0  
np = ' '
while True:
    print('--'*15)
    nome=str(input("Qual o nome do Produto? "))
    prec=float(input("Qual o preço do produto? R$"))
    print('--'*15)
    esc=' '
    while esc not in 'SN':
        esc=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    cont += 1
    if cont == 1:
        mprec = prec
        np=nome
    som += prec
    if prec > 1000:
        prod += 1
    if prec < mprec:
        mprec=prec
        np=nome
    if esc == 'N':
        break
print(f"O total de gasto foi; {som}")
print(f"{prod} Produto(s) custa(m) mais que mil reais.")
print(f"O produto mais barato foi {np} que custa R${mprec} reais")
