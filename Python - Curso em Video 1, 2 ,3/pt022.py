print("########## DESAFIO 26 ##########\n")
f = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes.'.format(f.count('A')))
print('A posição da primeira letra A é {}'.format(f.find('A')+1))
print('A posição da ultima letra A é {}'.format(f.rfind('A')+1))
