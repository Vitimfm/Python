from math import sqrt

a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = b**2 - 4*a*c

x1 = (-b - sqrt(delta))/(2*a)
x2 = (-b + sqrt(delta))/(2*a)
x3 = (-b)/(2*a)

if a == 0:
    print('Não é equação do segundo grau, pois a = 0')
elif delta < 0:
    print('Não existe raiz real para delta')
elif delta == 0:
    print('Raiz única')
    print(x3)
else:
    print('Duas raizes')
    print(f'X1 é {x1} e X2 é {x2}')

