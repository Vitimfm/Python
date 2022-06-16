'''Receber um Vetor do usuário'''

lista = []
quant = int(input('Quantidade de nº do vetor: '))
for i in range(1, quant + 1):
    valor = float(input(f'{i}º valor: '))
    lista.append(valor)
    
'''Media_par'''

count = 0
soma = 0
for i in lista:
    if i % 2 == 0:
        soma += i
        count += 1
if count == 0:
    print('Nenhum numero par.')
else:
    media = soma / count
    print(f'Media dos nº pares: {media:.1f}') 
    

        