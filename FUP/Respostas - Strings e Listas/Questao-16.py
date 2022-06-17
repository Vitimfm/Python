lista = []

x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = int(input(f'{i}º valor: '))
    lista.append(val)


def menorFrente(l):
    print(f'Lista inserida: {l}')
    lis = []
    while len(l) > 0:
        min = l[0]
        for i in l:
            if i < min:
                min = i
        lis.append(min)
        l.remove(min)       
    return lis

print(menorFrente(lista))