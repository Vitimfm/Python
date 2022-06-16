'''Receber um Vetor do usuário'''

lista = []
quant = int(input('Quantidade de nº do vetor: '))
for i in range(1, quant + 1):
    valor = int(input(f'{i}º valor: '))
    lista.append(valor)
    
print(f'Vetor inserido: {lista}')

'''Maior_posicao'''

max = lista[0]
posMaior = 0
for i in range(quant):
    if lista[i] > max:
        max = lista[i]
        posMaior = i
    
print(f'Maior valor: {max}')
print(f'Indice do maior: {posMaior}')