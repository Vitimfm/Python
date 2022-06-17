
# Solução muito questionável...

x1 = int(input('Digite o valor de x1: '))
y1 = int(input('Digite o valor de y1: '))

x2 = int(input('Digite o valor de x2: '))
y2 = int(input('Digite o valor de y2: '))

x3 = int(input('Digite o valor de x3: '))
y3 = int(input('Digite o valor de y3: '))

if x1 > x2 and x1 > x3:
    if x2 > x3:
        largura = x1 - x3
    else:
        largura = x1 - x2
elif x2 > x1 and x2 > x3:
    if x1 > x3:
        largura = x2 - x3
    else:
        largura = x2 - x1
elif x3 > x1 and x3 > x2:
    if x1 > x2:
        largura = x3 - x2
    else:
        largura = x3 - x1
elif x1 == x2 and x2 == x3 and x3 == x1:
    print('Retangulo invalido')

if y1 > y2 and y1 > y3:
    if y2 > y3:
        altura = y1 - y3
    else:
        altura = y1 - y2
elif y2 > y1 and y2 > y3:
    if y1 > y3:
        altura = y2 - y3
    else:
        altura = y2 - y1
elif y3 > y1 and y3 > y2:
    if y1 > y2:
        altura = y3 - y2
    else:
        altura = y3 - y1
elif y1 == y2 and y2 == y3 and y3 == y1:
    print('Retangulo invalido')

if largura == 0 or altura == 0:
    print('Retangulo invalido')
else:
    print(f'Largura é de {largura} e altura é de {altura}.')

