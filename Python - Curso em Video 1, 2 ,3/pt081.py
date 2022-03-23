print('\033[1;33m##### DESAFIO 80 #####\033[m\n')
lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        #print('Adicionado no final da Lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                #print(f'Adcionado na posição: {pos}')
                break
            pos += 1
            
print(lista)
