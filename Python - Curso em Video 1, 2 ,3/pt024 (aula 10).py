n1 = float(input("Digite sua nota: "))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m >= 8.0:
    print('{} Que notão, c é brabo!'.format(m))
if m >= 7.0:
    print('{} uuuuuh, foi quase, mano!'.format(m))
else:
    print('{}? Tu é um fudido mesmo né'.format(m))

