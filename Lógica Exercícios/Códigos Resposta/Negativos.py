'''Receber um Vetor do usuário'''

lista = []
quant = int(input('Quantidade de nº do vetor: '))
for i in range(1, quant + 1):
    valor = int(input(f'{i}º valor: '))
    lista.append(valor)
    
print(f'Vetor inserido: {lista}')


'''Negativos'''

print('Negativos: ')
for i in lista:
    if i < 0:
        print(i)
        
   
