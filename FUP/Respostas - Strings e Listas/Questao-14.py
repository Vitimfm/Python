lista = []
x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = int(input(f'{i}º valor: '))
    lista.append(val)


i = int(input('Inicio: '))
f = int(input('Fim: '))

def slice(l, i, f):
    lis = []
    for j in range(i, f):
        lis.append(l[j])
    return lis

print(slice(lista, i, f))