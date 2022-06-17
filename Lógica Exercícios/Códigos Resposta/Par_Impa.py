try:
    n = int(input('Digite a quantidade de numeros: '))
    for i in range(1, n + 1):
        x = float(input(f'Digite o {i}º número: '))
        if x % 2 == 0 and x > 0:
            print('Par e positivo.')
        elif x == 0:
            print('Nulo')
        elif x % 2 == 0 and x < 0:
            print('Par e negativo.')
        elif x % 2 != 0 and x > 0:
            print('Impar e positivo.')
        else:
            print('Impar e negativo.')
except:
    print('Insira apenas números.')
        
        