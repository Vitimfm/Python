while True:
    x = ''
    soma = 0
    try:
        x = int(input('Valor: '))
        if x == 0:
            break
        y = int(input('Nº repitições: '))
        
        if x % 2 == 0:
            temp = x
            print(f'{x} ', end='')
            for i in range(y - 1):
                x += 2
                soma += x
                print(f' {x} ', end='')
            print(f'\nSoma = {soma + temp}')
        else: 
            x += 1
            temp = x
            print(f'{x} ', end='')
            for i in range(y - 1):
                x += 2
                soma += x
                print(f' {x} ', end='')
            print(f'\nSoma = {soma + temp}')  
    except:
        print('Digite apenas números.')
                