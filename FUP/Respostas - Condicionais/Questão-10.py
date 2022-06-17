print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')

escolha = int(input('Escolha um operador: '))

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

if escolha < 1 or escolha > 4:
    print('Operador invalido')
elif escolha == 1:
    print(num1 + num2)
elif escolha == 2:
    print(num1 - num2)
elif escolha == 3:
    print(num1 * num2)
else:
    print(num1 / num2)

