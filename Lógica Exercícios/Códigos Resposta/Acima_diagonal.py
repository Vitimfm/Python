n = int(input('Qual a ordem da matriz: '))
if 0 <= n <= 10:
    
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
    soma = 0
    for i in range(n):
        for j in range(i+ 1,n):
       #for j in range(n):
           #if j > i:
            soma += matriz[i][j]
        
    print(f"Soma acima diagonal principal: {soma}")
                