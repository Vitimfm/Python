valor = int(input('Digite o valor inicial: '))
razao = int(input('Digite a razão: '))
quant = int(input('Digite a quantidade de elementos: '))
q = valor + quant * razao
for i in range(valor, q, razao):
    print(i, end=" ")
