try:  
    n = int(input('Entre com a quantidade de casos: '))

    soma = 0
    coe = 0
    sapo = 0
    rato = 0

    def porcentagem(x):
            porcen = x / soma * 100
            return porcen

    for i in range(1, n + 1):
        cob = int(input(f'Quantidade de cobaias no {i}º caso: '))
        tip = str(input(f'Tipo de cobaia no {i}º caso: '))
        soma += cob
        if tip.lower() == 'c':
            coe += cob
        elif tip.lower() == 'r':
            rato += cob
        elif tip.lower() == 's':
            sapo += cob
        else:
            print('Entre com uma cobaia entre: Sapo(S), Rato(R), Coelho(C).')
            continue
              
    print(f'=== Relatório Final] ===')
    print(f'Total de cobaias: {soma}')
    print(f'Total de coelhos: {coe}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}')
    print(f'Porcentagem de coelhos: {porcentagem(coe):.2f}')
    print(f'Porcentagem de rato: {porcentagem(rato):.2f}') 
    print(f'Porcentagem de sapo: {porcentagem(sapo):.2f}')      
          
except:
    print('Entre com valores válidos.')
   