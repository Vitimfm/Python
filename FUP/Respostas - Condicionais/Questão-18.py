x1 = int(input('Digite o valor de x1: '))
y1 = int(input('Digite o valor de y1: '))

x2 = int(input('Digite o valor de x2: '))
y2 = int(input('Digite o valor de y2: '))

x3 = int(input('Digite o valor de x3: '))
y3 = int(input('Digite o valor de y3: '))

if x2 > x1 and y2 > y1:
    print(f'Os pontos ({x1},{y1}) e ({x2},{y2}) podem formar um retangulo.')
    if x3 > x2 or x3 < x1:
        print(f'O ponto ({x3},{y3}) não está dentro do retangulo')
    elif y3 > y2 or y3 < y1:
        print(f'O ponto ({x3},{y3}) não está dentro do retangulo')
    else:
        print(f'O ponto ({x3},{y3}) está dentro do retangulo')
elif x2 == x1 or y2 == y1:
    print(f'Os pontos ({x1},{y1}) e ({x2},{y2}) desenham uma reta.')
else:
    print(f'Os pontos ({x1},{y1}) e ({x2},{y2}) não podem formar um retangulo.')

'''
ax = float(input('Coordenada x de A: '))
ay = float(input('Coordenada y de A: '))
bx = float(input('Coordenada x de B: '))
by = float(input('Coordenada y de B: '))
cx = float(input('Coordenada x de C: '))
cy = float(input('Coordenada y de C: '))

if ax < bx and ay < by:
    if (ax <= cx <= bx and ay <= cy <= by):
        print('C está contido')
    else:
        print('C não está contido')
else:
    print('Retângulo inválido')
'''


