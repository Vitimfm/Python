n = int(input('Digite o numero n: '))
soma = 0
for i in range(n):
    if i % 2 != 0:
        print(i)
        soma += i
print(f'A soma é {soma}')