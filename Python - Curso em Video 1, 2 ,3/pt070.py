print('\033[1;33m##### DESAFIO 70 #####\033[m\n')
print("=="*20)
val=int(input("Qual valor deseja sacar? R$"))
print("=="*20)
total = val
ced=200
totced=0
while True:
    if total >= ced:
        total-=ced
        totced+=1
    else:
        if totced > 0:
            print(f"Você vai precisar de {totced} notas de {ced}")
        if ced == 200:
            ced=100
        elif ced==100:
            ced=50
        elif ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=1
        elif ced==1:
            ced=0
        totced=0
        if total == 0:
            break
print("=="*20)
print("Volte sempre!")