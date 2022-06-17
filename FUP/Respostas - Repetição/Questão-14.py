while True:
    print('=====Menu=====')
    print('1 - adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')
    n = int(input('Escolha uma opção: '))
    if n == 1:
        a = int(input('Digite o primeiro numero: '))
        b = int(input('Digite o segundo numero: '))
        print(a + b)
    elif n == 2:
        a = int(input('Digite o primeiro numero: '))
        b = int(input('Digite o segundo numero: '))
        print(a - b)
    elif n == 3:
        a = int(input('Digite o primeiro numero: '))
        b = int(input('Digite o segundo numero: '))
        print(a * b)
    elif n == 4:
        a = int(input('Digite o primeiro numero: '))
        b = int(input('Digite o segundo numero: '))
        print(a / b)
    else:
        break
