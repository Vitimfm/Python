n = int(input('Ordem da matriz: '))

if 0 <= n <= 10:
    
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    vetor = []

    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
    print('Maior elemento de cada linha: ')
    
    for i in range(n):
        max = matriz[i][0]
        for j in range(1, n):
            if matriz[i][j] > max:
                max = matriz[i][j]
        
        vetor.append(max)
    
    for i in range(n):
        print(vetor[i])
            
    
    