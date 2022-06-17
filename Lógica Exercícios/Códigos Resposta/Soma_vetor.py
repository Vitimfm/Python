'''Receber um Vetor do usuário'''

lista = []
quant = int(input('Quantidade de nº do vetor: '))
for i in range(1, quant + 1):
    valor = float(input(f'{i}º valor: '))
    lista.append(valor)
    
print(f'Vetor inserido: {lista}')

'''Soma_vetor'''

soma = 0
media = 0
count = 0
for i in lista:
    soma += i 
    count += 1
    media = soma / count

print(f'Soma: {soma}\nMédia: {media:.2f}')