print(f'\033[1;33m{" DESAFIO 90 ":#^30}\033[m')
bolet = {}
bolet['nome'] = str(input('Nome do aluno: '))
bolet['Media'] = float(input('Média: '))
print(f'A média do(a) {bolet["nome"]} é: {bolet["Media"]}')
print('Ele(a) está ', end='')
if bolet['Media'] >= 7:
    print('aprovado(a)\n')
elif 5<= bolet["aluno"] < 7:
    print('de recuperação')
else:
    print('reprovado(a)\n')
