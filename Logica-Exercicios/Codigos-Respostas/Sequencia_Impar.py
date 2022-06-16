try:
    x = int(input('Insira um numero: '))
    for i in range(x + 1):
        if i % 2 != 0:
            print(i)
except:
    print('Insira apenas numeros.')