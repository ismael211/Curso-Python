#LISTAS
lanche = ['suco', 'Pizza', 'hamburger', 'pudim']

# lanche[0]= 'picole' para alterar um item especifico da lista
# lanche.append('Cookie') adciona um item no final da lista
#  lanche.insert(3,'Pao') para inserir um item em tal posição

''' Para remover algo
del(lanche[4])
lanche.pop(4)
lanche.remove(suco)'''

# valores = list(range(3, 10)) criando uma lista com números

# valores.sort() Para ordenar uma lista
# valores.sort(reverse=True) Para ordenar ao contrario
# len(valores) Saber o tamanho de uma lista

val = [1]
for c in range(0, 3):
    val.append(int(input('Digite um número: ')))
for pos, v in enumerate(val):
    print(f'Na posição {pos} encontrei o valor: {v}')

a = [1, 2, 3, 4]
b = a[:] #Jeito certo de criar uma cópia
