from datetime import date
print(f'\033[1;33m{" DESAFIO 92 ":#^30}\033[m\n')
ano = date.today().year
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = ano - nasc
dados['ctps'] = int(input('Nº da carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados ['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Seu salario: R$'))
    dados ['aposentadoria'] =  dados['idade'] + (dados['contratação'] + 35) - ano
print('=-'*25)
for k, v in dados.items():
    print(f'{k}: {v}')
