print('\033[1;33m##### DESAFIO 70 #####\033[m\n')

print("=="*20)
val=int(input("Digite um valor em centavos? R$"))
print("=="*20)

totcent = val

totum = 0
totcinc = 0
totdez = 0
totvint = 0
totcinq = 0
totumreal = 0

if totcent >= 100:
    totumreal = int(totcent/100)
    totcent = val-(totumreal*100)


if totcent >= 50:
    total = totcent
    totcinq = int(totcent/50)
    totcent -= (totcinq*50)


if totcent >= 20:
    total = totcent
    totvint = int(totcent/20)
    totcent -= (totvint*20)


if totcent >= 10:
    total = totcent
    totdez = int(totcent/10)
    totcent -= (totdez*10)


if totcent >= 5:
    total = totcent
    totcinc = int(totcent/5)
    totcent -= (totcinc*5)

if totcent >= 1:
    totum = totcent


print(f"Para {val} será preciso: \n{totumreal} moedas de 1 real")
print(f"\n{totcinq} moedas de 50 centavos")
print(f"\n{totvint} moedas de 20 centavos")
print(f"\n{totdez} moedas de 10 centavos")
print(f"\n{totcinc} moedas de 5 centavos")
print(f"\n{totum} moedas de 1 centavos")



print("Volte sempre!")