lista = []
x = int(input('Quantidade de nº da lista: '))
for i in range(1, x + 1):
    val = int(input(f'{i}º valor: '))
    lista.append(val)
y = int(input('Valor comparável: '))


def divideNumeros(l, p):
    menor = []
    maior = []
    for i in l:
        if i < p:
            menor.append(i)
        else:
            maior.append(i)
    return (menor, maior)

print(divideNumeros(lista, y))
        
    