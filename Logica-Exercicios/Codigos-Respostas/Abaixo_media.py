'''Receber um Vetor do usuário'''

lista = []
quant = int(input('Quantidade de nº do vetor: '))
for i in range(1, quant + 1):
    valor = float(input(f'{i}º valor: '))
    lista.append(valor)

'''Abixo_media'''

count = 0
soma = 0
for i in lista:
    soma += i
    count += 1
media = soma / count
print(f'Media do vetor: {media:.3f}')
for i in lista:
    if i < media:
        print(i)  
    

