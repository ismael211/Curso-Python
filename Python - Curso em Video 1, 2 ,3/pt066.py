print('\033[1;33m##### DESAFIO 67 #####\033[m\n')
print('Digite um número negativo para PARAR\n')
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("--"*15)
    if n < 0:
        print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
        break
    for c in range(1,10):
        print(f"{n} x {c} = {n*c}")
    print("--"*15)    