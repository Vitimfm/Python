lista = []
x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = int(input(f'{i}º valor: '))
    lista.append(val)


def contaPares(l):
    lis = []
    for i in l:
        if i % 2 == 0:
            lis.append(i)
    return lis

print(contaPares(lista))