def torreXadrez():
    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))

    #posições na mesma linha
    for i in range(1,9):
        if i != coluna:
            print(f'({linha},{i})',end=',')

    #posições na mesma coluna
    for i in range(1,9):
        if i != linha:
            print(f'({i},{coluna})',end=',')
    
    print()
torreXadrez()
    