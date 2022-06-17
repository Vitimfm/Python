def busca(l, x):
    if l.count(x) != 0:
        return True
    return False
 
lista = []  
for i in range(1, 5):
    b = int(input(f'Entre com o {i}º da lista: '))
    lista.append(b)

vali = int(input('Digite o validador: '))
print(busca(lista, vali))

