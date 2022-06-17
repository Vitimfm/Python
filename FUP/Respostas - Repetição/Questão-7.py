n = int(input('Digite n: '))
fat = 1
for i in range(1,n+1):
    fat *= i
print(f'O fatorial de {n} é igual a {fat}')
