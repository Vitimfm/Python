n = int(input('Qual a ordem da matriz: '))
if 0 <= n <= 10:
    matriz = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
            
    print('\nMatriz inserida: ')
    for i in range(n):
        for j in range(n):
            print(f'{matriz[i][j]} ', end='')
        print()       
            
            
    print('Diagonal principal:')
    for i in range(n):
        print(f'[{matriz[i][i]}] ', end='' )
    print()


    count = 0
    for i in range(n):
        for j in range(n):
            if matriz[i][j] < 0:
                count += 1
                
    print(f'Quantidade de números negativos: {count}')
else:
    print('Entre com valores entre 0-10')
