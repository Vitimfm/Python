from math import sqrt

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

delta = b**2 -4 * a * c

if a == 0 or delta < 0:
    print('- Não possui raizes reais')
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'x1 = {x1:.4f}' f'\nx2 = {x2:.4f}')
