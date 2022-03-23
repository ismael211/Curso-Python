print('\033[1;33m##### DESAFIO 83 #####\033[m\n')
pilha = []
exp = str(input('Digite uma expressão: '))
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão esta certa!')
else:
    print('Sua expressão está incorreta!')
    