try:
    n = int(input('Digite quantos casos você vai querer: '))
    for i in range(1, n + 1):
        x = float(input('Entre com o numerador: '))
        y = float(input('Entre com o denominador: '))
        if y == 0:
            print('Divisão Impossivel.')
        divisao = x / y 
        print(f'Divisão: {divisao:.1f}')
except:
    print('Entre com números válidos')