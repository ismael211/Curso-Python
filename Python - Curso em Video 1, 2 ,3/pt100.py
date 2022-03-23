print(f'\033[1;33m{" DESAFIO 96 ":#^30}\033[m\n')
def area(a, b):
    ar = a * b
    print(f'A área de um terreno {a}x{b} é: {ar}m²')


area(a=float(input('Largura: ')), b=float(input('Comprimento: ')))
