print(f'\033[1;33m{" DESAFIO 94 ":#^30}\033[m\n')
dados = {}
banco = []
sex = []
media = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = 'a'
    while dados['sexo'] not in 'FM':
        dados['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    banco.append(dados.copy())
    media += dados['idade']
    if dados['sexo'] == 'F':
        sex.append(dados['nome'])
    esc = 'a'
    while esc not in 'SN':
        esc = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if esc == 'N':
        break
print('=-'*16)
print(f'-- O grupo tem {len(banco)} pessoas')
media = media/len(banco)
print(f'-- A média de idade do grupo é {media}')
print(f'-- As mulheres cadastradas foram: {sex}')
print('-- Lista das pessoas que estão acima da média: \n')
for c in banco:
    if c['idade'] > media:
        print(f'Nome: {c["nome"]}; Sexo: {c["sexo"]}; Idade: {c["idade"]};')
print('\n>>>>ENCERRADO<<<<\n')
