lista = []
x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = float(input(f'{i}º Valor: '))
    lista.append(val)

print(lista)

def limites(l):
    max = l[0]
    min = l[0]
    for i in l:
        if i > max:
            max = i 
        if i < min:
            min = i 
    return (min, max)

print(limites(lista))
    