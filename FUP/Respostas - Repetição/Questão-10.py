a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
i = 1
while not (i % a == 0 and i % b == 0):
    i += 1
print(f'O mmc é {i}')