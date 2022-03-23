print(f'\033[1;33m{" DESAFIO 85 ":#^25}\033[m\n')
numbers = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        numbers[0].append(n)
    elif n % 2 != 0:
        numbers[1].append(n)
numbers.sort()
print(numbers)
print(f'Os números pares são: {numbers[0]}')
print(f'Os números impares são: {numbers[1]}')
