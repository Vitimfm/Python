try:
    n = int(input('Digite o fatorial desejado: '))
    if 0 < n < 15:
        fat = 1
        for i in range(1, n + 1):
            fat *= i
        print(f'O fatorial de {n} é {fat}')
except:
    print('Entre com números válidos.')