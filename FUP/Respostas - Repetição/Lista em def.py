'''
- Cada questão está dentro de uma função def questaox()
- Rodar o programa para escolher a questão desejada.
'''

def questao1():
    x = int(input('Digite um número n: '))
    i = 0
    while i <= x:
        print(i)
        i += 1
def questao2():
    x = int(input('Digite um número para ver sua tabuada: '))
    i = 0
    prod = i * x
    while i < 9:
        i += 1
        prod = i * x
        print(f'{x} * {i} = {prod}')
def questao3():
    x = 0
    for i in range(5):
        n = int(input('Digite um numero: '))
        if n > x:
            x = n
    print(x) 
def questao4():
    x = 0
    for i in range(10):
        n = int(input('Digite um numero: '))
        x += n
    print(x)
def questao5():
    soma = 0
    maior = 0
    d = int(input('Digite o numero de repetições: '))
    for i in range(d):
        n = int(input('Digite os numeros: '))
        soma += n
        if n > maior:
            maior = n
    print(f'O maior numero é {maior}')
    print(f'O somatorio é {soma}')
def questao6():
    x = 0
    n = 0
    while n >= 0:
        n = int(input('Digite um numero: '))
        x += n
    if n < 0:
        print(x)
def questao7():
    n = int(input('Digite n: '))
    fat = 1
    for i in range(1,n+1):
        fat *= i
    print(f'O fatorial de {n} é igual a {fat}')
def questao8():
    n = int(input('Digite o numero n: '))
    soma = 0
    for i in range(n):
        if i % 2 != 0:
            print(i)
            soma += i
    print(f'A soma é {soma}')
def questao9():
    n = int(input('Digite o numero n: '))
    for i in range(1,n+1):
        if n % i == 0:
            print(i)
def questao10():
    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo numero: '))
    i = 1
    while not (i % a == 0 and i % b == 0):
        i += 1
    print(f'O mmc é {i}')
def questao11():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite mais um número: '))

    max = n1 if n1 > n2 else n2
    min = n2 if n1 > n2 else n1

    rest = 0

    while min != 0:
     rest = max % min
     max = min
     min = rest

     print(f'MDC: {max}')  
def questao12():
    n = int(input('Digite um número: '))
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    print(primo)


    '''
    n = int(input('Digite um número: '))
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        print('Numero primo')
    elif n == 5 or n == 7 or n == 3 or n == 2:
        print('Numero primo')
    else:
    print('Numero não primo')
    '''
def questao13():
    valor = int(input('Digite o valor inicial: '))
    razao = int(input('Digite a razão: '))
    quant = int(input('Digite a quantidade de elementos: '))
    q = valor + quant * razao
    for i in range(valor, q, razao):
        print(i, end=" ")   
def questao14():
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
def questao15():
    n = int(input('Entre com um numero: '))
    print('=============')
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()
    print('=============')
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()
    print('=============')
    for i in range(1, n + 1):
        for j in range(i):
            print(' ', end='')
        print('*')
    print('=============')
    for i in range(n, 0, -1):
        for j in range(i):
            print(' ', end='')
        print('*')
    print('=============')
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()
    print('=============')
    for i in range(1, n + 1):
        for j in range(n - i):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()
    print('==============')
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for j in range(n):
            print('* ', end='')
        print()
    print('==============')
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(' ', end='')
        for j in range(i):
            print('* ', end='')
        print()
    print('==============')
    for i in range(n, 0, -1):
       for _ in range(n - i):
            print(' ', end='')
       for c in range(i):
           if c == 0 or c + 1 == i:
               print('* ', end='')
           else:
               print('  ', end='')
    print()
def questao16():
    n = int(input('Digite um numero: '))
    count = 1
    for i in range (1, n+1):
        for _ in range(i):
            print(count, end=' ')
            count += 1
        print() 
def questao17():
    n = int(input("Digite um número: "))
    res = 1
    for i in range(1, n + 1):
        res += 1 / i
    print(f'Resultado: {res:.2f}')
def questao18():
    n = int(input("Digite um número: "))
    res = 1
    count = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            res += 4 / count
        else:
            res -= 4 / count
        count += 2
    print(f'Resultado: {res:.2f}')
def questao19():
    n = int(input('Digite um valor n: '))
    valor = 1
    valorAntes = 0
    print('1', end=' ')
    for i in range(1, n):
        novoValor = valor
        valor = valor + valorAntes
        valorAntes = novoValor
        print(valor, end=' ')
def questao20():
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
def questao21():
    x = int(input('Coordenada X inicial: '))
    y = int(input('Coordenada Y inicial: '))

    print('Coordenadas possíveis: ')
    coord = ''

    for i in range(1, 9):
        if(y != i):
            coord += f'({x},{i}),'
            
        if(x != i):
            coord += f'({i},{y}),'
        
    print(coord.rpartition(',')[0])            
def questao22():
    alt = int(input('Digite a altura: '))
    x = 0
    for i in range(1, alt + 1):
        x += i ** 2

    print(x)
def questao23():
    n = int(input('Digite a quantidade de pontos: '))
    xmin = 0
    xmax = 0
    ymin = 0
    ymin = 0
    for i in range(1, n + 1):
        x = int(input(f'Digite a {i}º coordena de X: '))
        y = int(input(f'Digite a {i}º coordena de Y: '))
        
        
        if i == 1:
            xmax = xmin = x
            ymax = ymin = x
        else: 
            if x > xmax:
                xmax = x
            elif x < xmin:
                xmin = x
                
            if y > ymax:
                ymax = y
            elif y < ymin:
                ymin = y
        
    print(f'Ponto Mínimo: ({xmin},{ymin})')
    print(f'Ponto Máximo: ({xmax},{ymax})')
def questao24():
    ax = int(input('Digite a coordenada x: '))
    ay = int(input('Digite a coordenada y: '))

    bx = int(input('Digite um deslocamento para x: '))
    by = int(input('Digite um deslocamento para y: '))

    n = int(input('Digite o numero de pontos: '))

    for i in range(1, n + 1):
        ax += bx 
        ay += by
        print(f'Ponto({i}): [{ax},{ay}]') 
def questao25():
    '''
    [?]
    '''

    ax = int(input('Coordenada x: '))
    ay = int(input('Coordenada y: '))

    bx = int(input('Vetor deslocamento para x: '))
    by = int(input('Vetor deslocamento para y: '))

    xmin = int(input('Xmin da caixa: '))
    ymin = int(input('Ymin da caixa: '))

    xmax = int(input('Xmax da caixa: '))
    ymax = int(input('Xmax da caixa: '))

    n = int(input('Numero de pontos: '))

    while ax < xmax:
        ax += bx 
        ay += by
        colide = True
        if ax < xmax and ax > xmin and ay < ymax and ay > ymin:
            print('Colide')
            break
        else:
            colide = False

    if colide == False:
        print('Não colide')
def questao26():
    import turtle
    n = int(input('Digite o numeros de quadrados: '))
    main = turtle.Screen()
    main.setup(800, 600)

    caneta = turtle.Turtle()
    caneta.shape('arrow')
    caneta.speed(5)
    for _ in range(n):
        for i in range(2):
            caneta.forward(50)
            caneta.left(90)
            caneta.forward(50)
            caneta.left(90)
        caneta.forward(50)

    while True:
        main.update()
def questao27():
    import turtle
    n = int(input('Quantidade de lados do polígono: '))
    lado = int(input('Tamanho do lado: '))
    main = turtle.Screen()
    caneta = turtle.Turtle()

    for _ in range(n):
        caneta.forward(lado)
        caneta.right(360 / n)

    while True:
        main.update()
def questao28():
    import turtle
    camadas = int(input('Digite o numero de camadas: '))
    altura = int(input('Digite a altura: '))
    largura = int(input('Digite a largura: '))

    main = turtle.Screen()
    main.setup(800, 600)

    caneta = turtle.Turtle()
    caneta.shape('arrow')
    caneta.speed(5)

    for i in range(1, camadas + 1):
        for _ in range(2):
            caneta.forward(largura * i)
            caneta.right(90)
            caneta.forward(altura)
            caneta.right(90)
        caneta.right(90)
        caneta.forward(altura)
        caneta.left(90)

    while True:
        main.update()
def questao29():
    import turtle

    lado = int(input('Tamanho do lado: '))
    li = int(input('Quantidade de linhas: '))
    col = int(input('Quantidade de colunas: '))

    main = turtle.Screen()
    main.bgcolor('lightgray')
    caneta = turtle.Turtle()
    caneta.speed(0)
    caneta.up()
    caneta.goto(-200, 200)
    caneta.down()

    for c in range(li):
        for i in range(col):
            if i % 2 == 0:
                caneta.color('black')
            else:
                caneta.color('white')
            caneta.begin_fill()

            for _ in range(4):
                caneta.forward(lado)
                caneta.right(90)
            caneta.end_fill()
            caneta.forward(lado)

        if c % 2 == 0:
            caneta.right(90)
            caneta.forward(lado * 2)
            caneta.right(90)
        else:
            caneta.left(180)

    while True:
        main.update()

while True: 
    print('\n======================================')
    n = int(input('Escolha uma questão ou Sair(0): '))
    print('--------------------------------------')
    if n >= 0 and n <= 19:
        if n == 0:
            break
        if n == 1:
            questao1()
        elif n == 2:
            questao2()
        elif n == 3:
            questao3()
        elif n == 4:
            questao4()
        elif n == 5:
            questao5()
        elif n == 6:
            questao6()
        elif n == 7:
            questao7()
        elif n == 8:
            questao8()
        elif n == 9:
            questao9()
        elif n == 10:
            questao10()
        elif n == 11:
            questao11()
        elif n == 12:
            questao12()
        elif n == 13:
            questao13()
        elif n == 14:
            questao14()
        elif n == 15:
            questao15()
        elif n == 16:
            questao16()
        elif n == 17:
            questao17()
        elif n == 18:
            questao18()
        elif n == 19:
            questao19()
        elif n == 20:
            questao20()
        elif n == 21:
            questao21()
        elif n == 22:
            questao22()
        elif n == 23:
            questao23()
        elif n == 24:
            questao24()
        elif n == 25:
            questao25()
        elif n == 26:
            questao26()
        elif n == 27:
            questao27()
        elif n == 28:
            questao28()
        else:
            questao29()
    else:
        print('Escolha inválida')                                             
                        