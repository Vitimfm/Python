try:
    dentro = 0
    fora = 0
    n = int(input('Digite a quantidade de números: '))
    for i in range(1, n + 1):
        x = int(input(f'Digite o {i}º número: '))
        if 10 <= x <= 20:
            dentro += 1
        else:
            fora += 1
    print(f'Dentro: {dentro}\nFora: {fora}')
except:
    print('Digite apenas números inteiros')
        