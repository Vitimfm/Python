
p1 = 5.00
p2 = 3.50
p3 = 4.80
p4 = 8.90
p5 = 7.32

comprado = int(input("Digite o codigo do produto comprado: "))
quant = int(input("Digite a quantidade comprada: "))

if 1 <= comprado <= 5:
    if comprado == 1:
        pagar = p1 * quant
        print(f'Valor a pagar: R% {pagar:.2f}')
    elif comprado == 2:
        pagar = p2 * quant
        print(f'Valor a pagar: R% {pagar:.2f}')
    elif comprado == 3:
        pagar = p3 * quant
        print(f'Valor a pagar: R% {pagar:.2f}')
    elif comprado == 4:
        pagar = p4 * quant
        print(f'Valor a pagar: R% {pagar:.2f}')
    else:
        pagar = p5 * quant
        print(f'Valor a pagar: R% {pagar:.2f}')
else:
    print("Digite valores válidos")
