n = int(input('Digite a quantidade de pessoas: '))

alturas = []
generos = []

for i in range(1, n + 1):
    alt = float(input(f'Altura da {i}º pessoa: '))
    gen = str(input(f'Gênero da {i}º pessoa: '))
    alturas.append(alt)
    generos.append(gen)
     
min = alturas[0] 
max = alturas[0]
for i in range(n):
    if alturas[i] < min:
        min = alturas[i]
    elif alturas[i] > max:
        max = alturas[i]

print(f'Menor altura: {min}')
print(f'Maior altura: {max}')

count = 0
for i in generos:
    if i == 'M':
        count += 1

print(f'Numero de Homens: {count}')

soma = 0
count = 0
for i in range(n):
    if generos[i] == 'F':
        soma += alturas[i]
        count += 1

media = soma / count

print(f'Media altura das mulheres: {media:.2f}')
    
    