dados = []
pessoas = []
for c in range(0, 3):
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Idade: ')))
    dados.append(pessoas[:])
    pessoas.clear()
print(dados)