lista = []
x = int(input('Digite a quantidade de notas: '))
for i in range(1, x + 1):
    val = float(input(f'Entre com a {i}º nota: '))
    lista.append(val)

print(lista)

def media(l):
    soma = 0
    tol = 0
    for i in l:
        soma += i
        tol += 1
    med = soma / tol
    return print(f'{med:.2f}')

media(lista)

def outramedia():
    '''
    def media(l):
        lista = []
        soma = 0
        for i in range(1, l + 1):
            x = float(input(f'Entre com a {i}º nota: '))
            soma += x
            lista.append(x)
        med = soma / l
        print(lista)
        return print(f'{med:.2f}')

    x = int(input('Digite a quantidade de notas: '))
    media(x)
    '''
      