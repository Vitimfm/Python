try:
    n = int(input('Digite a tabuada desejada: '))
    for i in range(1, 11):
        prod = i * n
        print(f'{n} * {i} = {prod}')
except:
    print('Digite apenas números.')