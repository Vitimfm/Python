preco = float(input('Digite o preço do produto: '))
quant = int(input('Digite a quantidade comprada: '))
recebido = float(input('Digite o dinheiro recebido: '))

troco = recebido - (preco * quant) 

if troco >= 0:
    print(f'Troco: {troco:.2f}')
else:
    faltando = troco * -1
    print(f'Dinnheiro Insuficiente. Está faltando {faltando:.2f} R$')
