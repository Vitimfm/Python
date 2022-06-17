n = int(input("Digite um número: "))
res = 1
count = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        res += 4 / count
    else:
        res -= 4 / count
    count += 2
print(f'Resultado: {res:.2f}')
