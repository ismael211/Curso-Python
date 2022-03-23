print('###### DESAFIO 35 ######\n')
r1 = float(input('Reta um: '))
r2 = float(input('Reta dois: '))
r3 = float(input('Reta três: '))
if r1+r2 > r3 and r2+r3 > r1 and r1+r3 > r2:
    print('Essas retas \033[4;32mconseguem\033[m formar um triangulo!')
else:
    print('Essas retas \033[4;31mnão\033[m conseguem formar um triangulo.')