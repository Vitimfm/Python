min = int(input('Digite a quantidade de minutos: '))
if 0 <= min <= 100:
    print('Valor a pagar: 50 R$')
elif min > 100:
    n_min = (min - 100) * 2 + 50
    print(f'Valor a pagar: {n_min} R$')
else:
    print('Minutos inválidos')
    
    