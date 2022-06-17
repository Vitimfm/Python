from math import sqrt

cat1 = float(input("Digite o cateto 1: "))
cat2 = float(input("Digite o cateto 2: "))

hip = sqrt(cat1**2 + cat2**2)

print(f'Hipotenusa = {hip}')