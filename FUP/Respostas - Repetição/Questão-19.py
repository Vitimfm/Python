n = int(input('Digite um valor n: '))

valor = 1
valorAntes = 0
print('1', end=' ')
for i in range(1, n):
    novoValor = valor
    valor = valor + valorAntes
    valorAntes = novoValor
    print(valor, end=' ')
        