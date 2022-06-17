n = int(input('Serão digitados dados de quantos produtos: '))

comprados = []
vendidos = []

for i in range(1, n + 1):
    print(f'Produto {i}:')
    nome = str(input('Nome: '))
    compra = float(input('Preço de compra: '))
    venda = float(input('Preço de venda: '))
    comprados.append(compra)
    vendidos.append(venda)

print('=========================')

abaixo = 0
entre = 0
acima = 0

for i in range(n):
    lucro = vendidos[i] - comprados[i]
    perLucro = lucro * 100 / comprados[i]
    if perLucro < 10:
        abaixo += 1
    else:
        if perLucro <= 20:
            entre += 1
        else:
            acima += 1
            
print(f'Lucro abaixo de 10%: {abaixo}')
print(f'Lucro entre 10%-20%: {entre}')
print(f'Lucro acima de 20%: {acima}')
   
somaComprados = 0
for i in comprados:
    somaComprados += i
print(f'Valor total de compra: {somaComprados:.2f}')

somaVendidos = 0
for i in vendidos:
    somaVendidos += i
print(f'Valor total de venda: {somaVendidos:.2f}')

LucroTotal = somaVendidos - somaComprados
print(f'Lucro total: {LucroTotal:.2f}') 

print('=========================')
        