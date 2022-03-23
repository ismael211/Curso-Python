print(" ######## DESAFIO 22 ########\n")

nome = str(input('Digite seu nome completo: '))
print('Nome caixa alta: {}'.format(nome.upper()))
print('Nome caixa baixa: {}'.format(nome.lower()))
ce = nome.replace(' ', '')
print('Seu nome completo tem {} letras'.format(len(ce)))
fn = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(fn[0])))