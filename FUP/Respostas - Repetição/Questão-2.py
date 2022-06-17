x = int(input('Digite um número para ver sua tabuada: '))
i = 0
while i < 9:
    i += 1
    prod = i * x
    print(f'{x} * {i} = {prod}')
