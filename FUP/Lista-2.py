def questao1():
    num_1 = int(input('Digite o primeiro numero: '))
    num_2 = int(input('Digite o segundo numero: '))
    if num_1 > num_2:
        print(f'{num_1} é maior que {num_2}')
    elif num_1 == num_2:
        print('Numeros iguais')
    else:
        print(f'{num_2} é maior que {num_1}')
def questao2():
    '''
    Checando numero par ou impar
    '''

    num1 = int(input('Digite o numero: '))
    if num1 % 2 == 0:
        print('Numero par')
    else:
        print('Numero impar')
def questao3():
    num1 = int(input('Digite o 1 numero: '))
    num2 = int(input('Digite o 2 numero: '))

    if num1 == 0 or num2 ==0:
        print("0 é multiplo de todos os numeros")

    elif num1 > num2:
        if num1 % num2 ==0:
            print(f'{num1} é multiplo de {num2}')
        else:
                print(f'{num1} não é multiplo de {num2}')
    elif num1 < num2:
        print (f'{num1} não é multiplo de {num2}')
def questao4():
    print('Digite notas entre 0 e 10 para o cálculo da média.')

    nota1 = float(input('Digite o valor da primeira nota: '))
    nota2 = float(input('Digite o valor da segunda nota: '))
    nota3 = float(input('Digite o valor da terceira nota: '))
    media = (nota1 + nota2 + nota3)/3

    if nota1 >= 0 and nota1 <= 10:
        if nota2 >= 0 and nota2 <= 10:
            if nota3 >= 0 and nota3 <= 10:
                print(f'A média das notas é {media:.2f}')
                if media >= 7:
                    print('Aluno Aprovado.')
                elif media >= 4 and media < 7:
                    print('Aluno de Recuperação')
                else:
                    print('Aluno Reprovado')
            else:
                print("A terceira nota não está entre 0 e 10")
        else:
         print("A segunda nota não está entre 0 e 10")
    else:
        print("A primeira nota não está entre 0 e 10")
def questao5():
    print('Digite notas entre 0 e 10 para o cálculo da média.')

    nota1 = float(input('Digite o valor da primeira nota: '))
    nota2 = float(input('Digite o valor da segunda nota: '))
    nota3 = float(input('Digite o valor da terceira nota: '))
    media = (nota1 + nota2 + nota3)/3

    if nota1 >= 0 and nota1 <= 10:
        if nota2 >= 0 and nota2 <= 10:
            if nota3 >= 0 and nota3 <= 10:
                print(f'A média das notas é {media:.2f}')
                if media >= 7:
                    print('Aluno Aprovado.')
                elif media >= 4 and media < 7:
                    print('Aluno de Recuperação')
                else:
                    print('Aluno Reprovado')
            else:
                print("A terceira nota não está entre 0 e 10")
        else:
         print("A segunda nota não está entre 0 e 10")
    else:
        print("A primeira nota não está entre 0 e 10")             
def questao6():
    nota = float(input('Digite sua nota: '))
    if nota < 0 or nota > 10:
        print('Nota Invalida')
    elif nota >= 0 and nota <= 5:
        print('Conceito E')
    elif nota > 5 and nota <= 6:
        print('Conceito D')
    elif nota > 6 and nota <= 7:
        print('Conceito C')
    elif nota > 7 and nota <= 8:
        print('Conceito B')
    else:
        print('Conceito A')
def questao7():
    carac = str(input('Digite um caractere: '))
    if carac.isdigit():
        print('numero')
    elif carac == 'a' or carac == 'e' or carac == 'i' or carac == 'o' or carac == 'u':
        print('vogal')
    else:
            print('consoante')
def questao8():
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    num3 = int(input('Digite o terceiro numero: '))

    if num1 > num2 and num1 > num3:
        print(f'{num1} é o maior entre os três')
    elif num2 > num1 and num2 > num3:
        print(f'{num2} é o maior entre os três')
    else:
        print(f'{num3} é o maior entre os três')
def questao9():
    # Printar numero em ordem crescente

    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    num3 = int(input('Digite o terceiro numero: '))

    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print(num3)
            print(num2)
        else:
            print(num2)
            print(num3)
        print(num1)
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print(num3)
            print(num1)
        else:
            print(num1)
            print(num3)
        print(num2)
    elif num3 > num1 and num3 > num2:
        if num1 > num2:
            print(num2)
            print(num1)
        else:
            print(num1)
            print(num2)
        print(num3)



    '''
    Printar numero em ordem Decrescente

    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    num3 = int(input('Digite o terceiro numero: '))

    if num1 > num2 and num1 > num3:
        print(num1)
        if num2 > num3:
            print(num2)
            print(num3)
        else:
            print(num3)
            print(num2)
    elif num2 > num1 and num2 > num3:
        print(num2)
        if num1 > num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)
    elif num3 > num1 and num3 > num2:
        print(num3)
        if num1 > num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1)    
    '''
def questao10():
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')

    escolha = int(input('Escolha um operador: '))

    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))

    if escolha < 1 or escolha > 4:
        print('Operador invalido')
    elif escolha == 1:
        print(num1 + num2)
    elif escolha == 2:
        print(num1 - num2)
    elif escolha == 3:
        print(num1 * num2)
    else:
        print(num1 / num2)                
def questao11():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))

    if a >= b + c:
        print('O valor de a não é permitido como lado de um triangulo')
    elif b >= a + c:
        print('O valor de b não é permitido como lado de um triangulo')
    elif c >= b + a:
        print('O valor de c não é permitido como lado de um triangulo')
    elif a == b and b == c and c == a:
        print('Triangulo Equilátero')
    elif a != b and b != c and c != a:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isósceles')
def questao12():
    from math import sqrt

    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))

    delta = b**2 - 4*a*c

    x1 = (-b - sqrt(delta))/(2*a)
    x2 = (-b + sqrt(delta))/(2*a)
    x3 = (-b)/(2*a)

    if a == 0:
        print('Não é equação do segundo grau, pois a = 0')
    elif delta < 0:
        print('Não existe raiz real para delta')
    elif delta == 0:
        print('Raiz única')
        print(x3)
    else:
        print('Duas raizes')
        print(f'X1 é {x1} e X2 é {x2}')
def questao13():
    produto = input('Digite o nome do produto: ')
    massa_p1 = float(input('Digite a primeira massa do produto: '))
    preco_p1 = float(input('Digite o preço do produto: '))
    massa_p2 = float(input('Digite a segunda massa do produto: '))
    preco_p2 = float(input('Digite o preço do produto: '))

    if massa_p1 / preco_p1 > massa_p2 / preco_p2:
        print(f'O {produto} de {massa_p1}g por R$ {preco_p1:.2f} é mais vantajoso.')
    else:
        print(f'O {produto} de {massa_p2}g por R$ {preco_p2:.2f} é mais vantajoso.')
def questao14():
    codigo = int(input('Digite o código do produto: '))
    quanti = int(input('Digite a quantidade do produto comprado: '))

    if codigo < 1 or codigo > 40:
        print('Codigo invalido')
    elif codigo >= 1 and codigo <= 10:
        codigo = 10.0
    elif codigo >= 11 and codigo <= 20:
        codigo = 15.0
    elif codigo >= 21 and codigo <= 30:
        codigo = 20.0
    else:
        codigo = 30.0

    preco_t = codigo * quanti
    print(f'O preço unitário do produto foi de R$ {codigo}')
    print(f'O preço total do produto foi de R$ {preco_t}')

    if preco_t <= 250.0:
        desconto = preco_t * 5 / 100
        print(f'O produto teve um desconto de 5% = R$ {desconto}')
    elif preco_t > 250 and preco_t <= 500:
        desconto = preco_t * 10 / 100
        print(f'O produto teve um desconto de 10% = R$ {desconto}')
    else:
        desconto = preco_t * 15 / 100
        print(f'O produto teve um desconto de 15% = R$ {desconto}')

    preco_f = preco_t - desconto
    print(f'O preço final a ser pago é de R$ {preco_f}')
def questao15():
    dia = int(input('Digite o dia do seu aniversário: '))
    print('jan  fev  mar  abr')
    print('mai  jun  jul  ago')
    print('set  out  nov  dez')
    mes = str(input('Digite o mês do seu aniversário: '))

    if dia >= 1 and dia <=10:
        nome = ' de frag negativo'
    elif dia > 10 and dia <= 20:
        nome = 'camper'
    else:
        nome = 'que só morre'

    if mes == 'jan':
        print('Mago',nome)
    elif mes == 'fev':
        print('Arqueiro',nome)
    elif mes == 'mar':
        print('Suporte',nome)
    elif mes == 'abr':
        print('Bardo',nome)
    elif mes == 'mai':
        print('Sniper',nome)
    elif mes == 'jun':
        print('Guerreiro',nome)
    elif mes == 'jul':
        print('Fuzileiro',nome)
    elif mes == 'ago':
        print('Mvp',nome)
    elif mes == 'set':
        print('Barbaro',nome)
    elif mes == 'out':
        print('NPC',nome)
    elif mes == 'nov':
        print('PK',nome)
    else:
        print('Noob',nome)   
def questao16():
    salabase = float(input('Digite o salário-base: '))
    depen = int(input('Digite o numero de dependentes: '))

    salabruto = salabase + (depen * 120)

    if salabruto < 1000:
        IRRF = 0
        print('Isento de IRRF')
    elif salabruto >= 1000 and salabruto < 2500:
        IRRF = salabruto * 10 / 100
        print(f'IRRF de 10% = R$ {IRRF}')
    else:
        IRRF = salabruto * 20 / 100
        print(f'IRRF de 20% = R$ {IRRF}')

    salaliq = salabruto - IRRF

    if salaliq < 1750:
        print('Gratificação de R$ 500')
        salareceber = salaliq + 500
    else:
        print('Gratificação de R$ 500')
        salareceber = salaliq + 250

    print(f'O salário a receber é de R$ {salareceber}.')
def questao17():
    x = float(input('Digite x: '))
    y = float(input('Digite y: '))

    if x > 0 and y > 0:
        print('Primeiro quadrante')
    elif x < 0 and y > 0:
        print('Segundo quadrante')
    elif x < 0 and y < 0:
        print('Terceiro quadrante')
    elif x > 0 and y < 0:
        print('Quarto quadrante')
    else:
        print('O ponto está sobre um dos eixos')
def questao18():
    x1 = int(input('Digite o valor de x1: '))
    y1 = int(input('Digite o valor de y1: '))

    x2 = int(input('Digite o valor de x2: '))
    y2 = int(input('Digite o valor de y2: '))

    x3 = int(input('Digite o valor de x3: '))
    y3 = int(input('Digite o valor de y3: '))

    if x2 > x1 and y2 > y1:
        print(f'Os pontos ({x1},{y1}) e ({x2},{y2}) podem formar um retangulo.')
        if x3 > x2 or x3 < x1:
            print(f'O ponto ({x3},{y3}) não está dentro do retangulo')
        elif y3 > y2 or y3 < y1:
            print(f'O ponto ({x3},{y3}) não está dentro do retangulo')
        else:
            print(f'O ponto ({x3},{y3}) está dentro do retangulo')
    elif x2 == x1 or y2 == y1:
        print(f'Os pontos ({x1},{y1}) e ({x2},{y2}) desenham uma reta.')
    else:
        print(f'Os pontos ({x1},{y1}) e ({x2},{y2}) não podem formar um retangulo.')

    '''
    ax = float(input('Coordenada x de A: '))
    ay = float(input('Coordenada y de A: '))
    bx = float(input('Coordenada x de B: '))
    by = float(input('Coordenada y de B: '))
    cx = float(input('Coordenada x de C: '))
    cy = float(input('Coordenada y de C: '))

    if ax < bx and ay < by:
        if (ax <= cx <= bx and ay <= cy <= by):
            print('C está contido')
        else:
            print('C não está contido')
    else:
        print('Retângulo inválido')
    '''
def questao19():
    # Solução muito questionável...
    x1 = int(input('Digite o valor de x1: '))
    y1 = int(input('Digite o valor de y1: '))

    x2 = int(input('Digite o valor de x2: '))
    y2 = int(input('Digite o valor de y2: '))

    x3 = int(input('Digite o valor de x3: '))
    y3 = int(input('Digite o valor de y3: '))

    if x1 > x2 and x1 > x3:
        if x2 > x3:
            largura = x1 - x3
        else:
            largura = x1 - x2
    elif x2 > x1 and x2 > x3:
        if x1 > x3:
            largura = x2 - x3
        else:
            largura = x2 - x1
    elif x3 > x1 and x3 > x2:
        if x1 > x2:
            largura = x3 - x2
        else:
            largura = x3 - x1
    elif x1 == x2 and x2 == x3 and x3 == x1:
        print('Retangulo invalido')

    if y1 > y2 and y1 > y3:
        if y2 > y3:
            altura = y1 - y3
        else:
            altura = y1 - y2
    elif y2 > y1 and y2 > y3:
        if y1 > y3:
            altura = y2 - y3
        else:
            altura = y2 - y1
    elif y3 > y1 and y3 > y2:
        if y1 > y2:
            altura = y3 - y2
        else:
            altura = y3 - y1
    elif y1 == y2 and y2 == y3 and y3 == y1:
        print('Retangulo invalido')

    if largura == 0 or altura == 0:
        print('Retangulo invalido')
    else:
        print(f'Largura é de {largura} e altura é de {altura}.')

while True: 
    print('======================================')
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
        else:
            questao19()
    else:
        print('Escolha inválida')                         
                                  