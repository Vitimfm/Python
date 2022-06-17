l = int(input('Linhas da matriz: '))
c = int(input('Colunas da matriz: '))

if 0 <= l <= 10 and 0 <= c <= 10:
    
    matriz = [[0 for _ in range(c)] for _ in range(l)]

    for i in range(l):
        for j in range(c):
            matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
    print('Valores Negativos: ')
    
    for i in range(l):
        for j in range(c):
            if matriz[i][j] < 0:
                print(matriz[i][j])
else:
    print('Digite valores entre 0-10.')
    
    
                
            