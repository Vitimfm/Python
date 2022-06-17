while True:
    try:
        x = int(input('Digite um numero: '))
        y = int(input('Digite outro numero: '))
        soma = 0
        if x > y:
            for i in range(y + 1, x):
                if i % 2 != 0:
                    soma += i
            print(f'Soma dos Impares = {soma}')
            break
        else:
            for i in range(x + 1, y):
                if i % 2 != 0:
                    soma += i
            print(f'Soma dos Impares = {soma}')  
            break         
    except:
        print('Digite apenas números.')
