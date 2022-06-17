l = int(input('Linhas da matriz: '))
c = int(input('Colunas da matriz: '))

if 0 <= l <= 10 and 0 <= c <= 10:
    
    matriz = [[0 for _ in range(c)] for _ in range(l)]

    vetor = ['' for _ in range(l)]

    for i in range(l):
        print(f'Digite os elementos da {i + 1}º linha: ')
        soma = 0
        for j in range(c):
            matriz[i][j] = int(input(f'Elemento [{i},{j}]: '))
            soma += matriz[i][j]
        vetor[i] = soma

    print(f'Vetor gerado: {vetor}')
else:
    print('Entre com valores entre 0-10.')


    


        

        
