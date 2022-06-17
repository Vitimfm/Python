from random import randint

def numerosAlea(n, min, max):
    lista = []
    for _ in range(n):
        lista.append(randint(min, max-1))
    return lista 

n = int(input('Quantidade de nº: '))
min = int(input('min: '))
max = int(input('max: '))

print(numerosAlea(n, min, max))       