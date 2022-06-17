soma = 0
maior = 0
d = int(input('Digite o numero de repetições: '))
for i in range(d):
    n = int(input('Digite os numeros: '))
    soma += n
    if n > maior:
        maior = n
print(f'O maior numero é {maior}')
print(f'O somatorio é {soma}')