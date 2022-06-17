n = int(input('Digite um número: '))
primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
print(primo)


'''
n = int(input('Digite um número: '))
if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print('Numero primo')
elif n == 5 or n == 7 or n == 3 or n == 2:
    print('Numero primo')
else:
    print('Numero não primo')
'''