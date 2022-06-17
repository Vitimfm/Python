n = int(input('Qual a ordem da matriz: '))

if 0 <= n <= 10:
    
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            matriz[i][j] = float(input(f'Elemento [{i},{j}]: '))
            
    print('Matriz digitada: ')
    
    for i in range(n):
        for j in range(n):
            print(f' {matriz[i][j]}  ', end='')
        print()
    
    soma = 0  
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > 0:
                soma += matriz[i][j]
    
    print(f'Soma dos positivos: {soma:.2f}')
    
    n1 = int(input('Escolha uma linha: '))
    
    for i in range(n):
        print(f'{matriz[n1][i]:.1f}  ', end='')
        
    c1 = int(input('\nEscolha uma coluna: '))
    
    for i in range(n):
        print(f'{matriz[i][c1]:.1f}  ', end='')
    
    print('\nDiagonal principal:')
    
    for i in range(n):
        print(f'{matriz[i][i]}  ', end='')
        
    print('\nMatriz Alterada:')
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j] < 0:
                matriz[i][j] = matriz[i][j] ** 2
            print(f' {matriz[i][j]}  ', end='')
        print()      
                   