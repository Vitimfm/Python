def questaoIni():
    '''
    Variáveis Invalidas

    $salario    2vizinhos
    alfa 2      a+b
    a>b         a[1]
    u.f         salario$
    '''

    '''
    Variáveis Validas

    qwert       DiaAdia    guarda_chuva
    _o          xKH        bestaTeste
    val0r       valOr
    '''

    # Questão 2

    '''
    / - Divisão  // Divisão Inteira  % - Resto da Divisão
    a) -7        d) 21,7
    b) 1         e) -10,5
    c) 65,11     f) 0,04
    '''

    # Questão 3

    '''
    a) 0        e) 0,66
    b) 2        f) 0,66
    c) 3        g) 7
    d) 4,3
    '''

    # Questão 4

    '''
    a) True
    b) True
    c) True
    d) True                
    c) True
    '''
    print('Comentado no Código')
def questao5():
    print('Questão 5\nConverção Dolar - Real')
    dolar = float(input('Digite o valor em dolar: '))
    real = dolar * 3.92
    print(f'O valor US$ {dolar} equivale a R$ {real}')
def questao6():
    print('Leia um número inteiro e imprima o seu antecessor e seu sucessor')
    num = int(input('Digite um numero: '))
    anter = num - 1
    suces = num + 1
    print(f'Seu antecessor é {anter} e seu sucessor é {suces}')
def questao7():
    print('Leia os lados de um retângulo e retorne a sua área.')
    lado1 = int(input('Digite o primeiro lado do retangulo: '))
    lado2 = int(input('Digite o segundo lado do retangulo: '))
    area = lado1 * lado2
    print(f'A área do retangulo é {area}.')
def questao8():
    print('Leia um valor x e retorne sua aplicação na função f(x)=3x2−6x+5')
    x = int(input('Digite o valor de x: '))
    fun = 3 * x**2 -6*x + 5
    print(f'Valor de {x} na função é {fun}')   
def questao9():
    from math import sqrt

    print('Questão 9\nEquação do Segundo Grau')
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))

    delta = b**2 - 4*a*c

    x1 = (-b - sqrt(delta))/(2*a)
    x2 = (-b + sqrt(delta))/(2*a)

    print(f"O valor de delta é igual a {delta}")
    print(f"As raízes são iguais a {x1} e {x2}")
def questao10():
    print('Questão 10\nLeia os coeficientes A, B, e C e um valor x e retorne\no resultado de sua aplicação na função f(x)=Ax^2+Bx+C')
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))
    x = float(input('Digite o valor de x: '))

    fun = a*x**2 + b*x + c
    print(f'O resultado de x= {x} na função é de {fun}')
def questao11():
    print('Questão 11\nLeia dois catetos e retorne a hiportenusa.')
    from math import sqrt

    cat1 = float(input("Digite o cateto 1: "))
    cat2 = float(input("Digite o cateto 2: "))

    hip = sqrt(cat1**2 + cat2**2)

    print(f'Hipotenusa = {hip:.2f}')
def questao12():
    print('Questão 12\nGraus em Radianos')
    angulo_graus = float(input('Digite um angulo em graus: '))
    pi = 3.14
    rad = angulo_graus * (pi / 180)
    print(f'O valor do angulo {angulo_graus} em radianos é {rad:.2f}')        
def questao13():
    print('Questão 13\nCilindro circular reto')
    altura = float(input('Digite a altura do cilindro circular reto: '))
    raioB = float(input('Digite o raio da base do cilindro circular reto: '))

    pi = 3.14

    areaL = 2 * pi * raioB * altura
    areaB = pi * raioB**2
    volume = areaB * altura

    print(f'A área lateral é igual a {areaL}')
    print(f'A área da base é igual a {areaB}')
    print(f'O volume é igual a {volume}')       
def questao14():
    print('Questão 14\nLeia as coordenadas (x,y) de um ponto e retorne a sua distância até a\norigem do sistema de coordenadas')
    from math import sqrt
    x = int(input('Digite o valor de x: '))
    y = int(input('Digite o valor de y: '))

    hip = sqrt(x**2 + y**2)

    print(f'A distancia é {hip}')        
def questao15():
    print('Questão 15\nDistância entre dois pontos')
    from math import sqrt
    x1 = int(input('Digite o valor de x1: '))
    y1 = int(input('Digite o valor de y1: '))
    x2 = int(input('Digite o valor de x2: '))
    y2 = int(input('Digite o valor de y2: '))

    cat1 = x2 - x1
    cat2 = y2 - y1

    distancia = sqrt(cat1**2 + cat2**2)

    print(f'A distancia entre os dois pontos é {distancia}')
def questao16():
    print('Questão 16\nImposto de 40% sobre um produto')
    valor = float(input('Digite o valor de acessorio: '))
    imposto = valor * 40 / 100
    print(f'O valor repassado ao governo é de {imposto}')    
def questao17():
    print('Questão 18\nCrédito rotativo')
    usadoMarço = float(input('Digite o valor usado no mês de Março: '))
    pagoMarço = float(input('Digite o valor pago no mês de Março: '))
    usadoAbril = float(input('Digite o valor usado no mês de Abril: '))

    restante = usadoMarço - pagoMarço

    FaturaAbril = usadoAbril + restante + (restante * 3.3 / 100)

    print(f'Fatura de abril é {FaturaAbril}')  
def questao18():
    print('Questão 18\nFaça um programa que leia um número inteiro positivo de 4 dígitos e imprima 1 dígito por linha')
    digito = input('Digite um numero de 4 digitos: ')
    print(digito[0])
    print(digito[1])
    print(digito[2])
    print(digito[3])
def questao19():
    print('Questão 19\nFaça um programa que leia um número inteiro positivo de três dígitos e imprima o número\nformado pelos dígitos invertidos do número lido')
    numero = int(input('Digite 3 digitos: '))
    numero_i = int(str(numero)[::-1])
    print(numero_i)  
           
while True: 
    print('======================================')
    n = int(input('Escolha uma questão ou Sair(0): '))
    print('--------------------------------------')
    if n >= 0 and n <= 19:
        if n == 0:
            break
        if n == 1 or n == 2 or n == 3 or n == 4:
            questaoIni()
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
        else:
            questao19()
    else:
        print('Escolha inválida') 
