l = int(input('Linhas da matriz: '))
c = int(input('Colunas da matriz: '))

if 0 <= l <= 10 and 0 <= c <= 10:
    
    matriz1 = [[0 for _ in range(c)] for _ in range(l)]
    matriz2 = [[0 for _ in range(c)] for _ in range(l)]
    matriz3 = [[0 for _ in range(c)] for _ in range(l)]

    print('Digite valores da matriz A:')
    for i in range(l):
        for j in range(c):
            matriz1[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
    print('Digite valores da matriz B:')
    for i in range(l):
        for j in range(c):
            matriz2[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
    print('Matriz Soma:')
    for i in range(l):
        for j in range(c):
            matriz3[i][j] = matriz1[i][j] + matriz2[i][j]
            print(f'{matriz3[i][j]} ', end='')
        print()
            
            
    
    
            