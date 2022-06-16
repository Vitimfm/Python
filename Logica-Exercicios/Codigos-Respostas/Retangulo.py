from math import sqrt

base = float(input('Digite a base do retangulo: '))
altura = float(input('Digite a altura do retangulo: '))

area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = sqrt(base**2 + altura**2)

print(f'Área: {area:.4f}')
print(f'Perimetro: {perimetro:.4f}')
print(f'Diagonal: {diagonal:.4f}')

