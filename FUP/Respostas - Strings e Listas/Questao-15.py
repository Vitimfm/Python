lista = []
x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = int(input(f'{i}º valor: '))
    lista.append(val)


def menorFrente(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    l.remove(min)
    l.insert(0, min)
    return l

print(menorFrente(lista))
            
   