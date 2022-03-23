from math import radians, sin, cos, tan
print('######### DESAFIO 18 #########\n')
n = float(input('Digite um número: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print(f'O angulo de {n} tem o seno {s:.2f}')
print(f'O angulo de {n} tem o cosseno {c:.2}')
print(f'O angulo de {n} tem a tangente {t:.2}')