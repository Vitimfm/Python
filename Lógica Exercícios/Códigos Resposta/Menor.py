a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

if a < b and a < c:
    print(f'Menor: {a}')
elif b < a and b < c:
    print(f'Menor: {b}')
elif a == b == c: 
    print('Não há menor, pois todos são iguais.')
else:
    print(f'Menor: {c}')