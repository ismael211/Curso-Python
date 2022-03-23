test = list()
film = {'titulo':'Star Wars',
'ano':1977,
'Diretor':'George Lucas'
}
fil = {'titulo':'Jogador Nº 1', 'ano':2018, 'Diretor':'Steven Spielberg'}
test.append(film)
test.append(fil)
'''print()
print(filmes['ano'])
print()'''

print(film.values())
print(film.keys())
print(film.items())
#del film['ano'] apagar uma chave com o valor
#film ['ano']=  1976 trocar o valor de uma chave
film ['bilheteria'] = 200.00000 #adicionando uma chave e valor
print()
for k, v in film.items():
    print(f'{k} = {v}')
print()
'''print(test[0])
print(test[1])'''

estado = {}
brasa = []
for c in range(0, 3):
    estado['uf'] = str(input('Qual o estado? '))
    estado['sigla'] = str(input('Qual a sigla? '))
    brasa.append(estado.copy())
for c in brasa:
    for k in c.values(): 
        print(k, end=' ')
    print()
