n = int(input('Quantos valores terá cada vetor: '))
print('Valores do vetor A')
l1 = []
for i in range(1, n + 1):
    x1 = int(input(f'{i}º valor: '))
    l1.append(x1)

print('Valores do vetor B')
l2 = []
for i in range(1, n + 1):
    x2 = int(input(f'{i}º valor: '))
    l2.append(x2)

print('Vetor resultante: ')
soma = 0
l3 = []
for i in range(n):
    soma = (l2[i] + l1[i])
    l3.append(soma)
    
print(l3)