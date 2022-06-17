lista = []
x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = int(input(f'{i}º valor: '))
    lista.append(val)

print(lista)


def contaPares(l):
    par = 0
    for i in l:
        if i % 2 == 0:
            par += 1
    return par

print(contaPares(lista))
            
            
    