'''while True:
    text = str(input("Say something: "))
    if text == 'edileusa':
        break
    print(f'Você digitou: {text}')'''
print('\033[1;33m##### DESAFIO 66 #####\033[m\n')
    # condição de parada, soma e quantidade de números usados
som = 0
cont = 0
print("Type 999 for stop")
while True:
    n = int(input("Type a number: "))
    if n == 999:
        break
    som += n
    cont += 1
print(f"A soma dos {cont} numeros é igual á: {som}!")    