from math import sqrt
x1 = int(input('Digite o valor de x1: '))
y1 = int(input('Digite o valor de y1: '))
x2 = int(input('Digite o valor de x2: '))
y2 = int(input('Digite o valor de y2: '))

cat1 = x2 - x1
cat2 = y2 - y1

distancia = sqrt(cat1**2 + cat2**2)

print(f'A distancia entre os dois pontos é {distancia}')