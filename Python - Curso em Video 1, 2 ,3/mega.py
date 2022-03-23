import random
lista = 0
p = 0
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
       22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
for m in range(1, 5):
       a = random.choice(lis)
       b = random.choice(lis)
       c = random.choice(lis)
       d = random.choice(lis)
       e = random.choice(lis)
       f = random.choice(lis)
       lista = [a, b, c, d, e, f]
       lista.sort()
       print(f'O número sorteado foi: {lista}')
       lista.clear()
