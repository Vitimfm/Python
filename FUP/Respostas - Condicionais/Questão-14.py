
# Faltando correçao de erro para 'codigo < 1 or codigo > 40'

codigo = int(input('Digite o código do produto: '))
quanti = int(input('Digite a quantidade do produto comprado: '))

if codigo < 1 or codigo > 40:
    print('Codigo invalido')
elif codigo >= 1 and codigo <= 10:
    codigo = 10.0
elif codigo >= 11 and codigo <= 20:
    codigo = 15.0
elif codigo >= 21 and codigo <= 30:
    codigo = 20.0
else:
    codigo = 30.0

preco_t = codigo * quanti
print(f'O preço unitário do produto foi de R$ {codigo}')
print(f'O preço total do produto foi de R$ {preco_t}')

if preco_t <= 250.0:
    desconto = preco_t * 5 / 100
    print(f'O produto teve um desconto de 5% = R$ {desconto}')
elif preco_t > 250 and preco_t <= 500:
    desconto = preco_t * 10 / 100
    print(f'O produto teve um desconto de 10% = R$ {desconto}')
else:
    desconto = preco_t * 15 / 100
    print(f'O produto teve um desconto de 15% = R$ {desconto}')

preco_f = preco_t - desconto
print(f'O preço final a ser pago é de R$ {preco_f}')






