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
