num_1 = int(input('Digite o primeiro numero: '))
num_2 = int(input('Digite o segundo numero: '))
if num_1 > num_2:
    print(f'{num_1} é maior que {num_2}')
elif num_1 == num_2:
    print('Numeros iguais')
else:
    print(f'{num_2} é maior que {num_1}')