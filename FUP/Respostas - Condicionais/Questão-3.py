num1 = int(input('Digite o 1 numero: '))
num2 = int(input('Digite o 2 numero: '))

if num1 == 0 or num2 ==0:
    print("0 é multiplo de todos os numeros")

elif num1 > num2:
    if num1 % num2 ==0:
        print(f'{num1} é multiplo de {num2}')
    else:
            print(f'{num1} não é multiplo de {num2}')
elif num1 < num2:
    print (f'{num1} não é multiplo de {num2}')