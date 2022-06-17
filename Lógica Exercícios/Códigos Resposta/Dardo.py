d1 = float(input('Digite a primeira distancia: '))
d2 = float(input('Digite a segunda distancia: '))
d3 = float(input('Digite a terceira distancia: '))

if d1 > d2 and d1 > d3:
    print(f'Maior: {d1}')
elif d2 > d1 and d2 > d3:
    print(f'Maior: {d2}')
elif d1 == d2 == d3: 
    print('Três distancias iguais.')
else:
    print(f'Maior: {d3}')
    
