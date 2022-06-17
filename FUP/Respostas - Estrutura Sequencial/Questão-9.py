from math import sqrt

a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = b**2 - 4*a*c

x1 = (-b - sqrt(delta))/(2*a)
x2 = (-b + sqrt(delta))/(2*a)

print(f"O valor de delta é igual a {delta}")
print(f"As raízes são iguais a {x1} e {x2}")