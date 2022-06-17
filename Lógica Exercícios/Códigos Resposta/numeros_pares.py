'''Receber um Vetor do usuário'''

lista = []
quant = int(input('Quantidade de nº do vetor: '))
for i in range(1, quant + 1):
    valor = int(input(f'{i}º valor: '))
    lista.append(valor)
    
print(f'Vetor inserido: {lista}')

'''Numeros_pares'''
count = 0
for i in lista:
    if i % 2 == 0:
        count += 1
        print(i, end=' ')
        

print(f'\nNúmero de pares: {count}')