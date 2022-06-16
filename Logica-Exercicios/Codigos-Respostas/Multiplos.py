x = int(input('Digite um numero inteiro: '))
y = int(input('Digite outro numero inteiro: '))

if x > y: 
    if x % y == 0:
        print('São multiplos')
    else:
        print('Não multiplos')
        
if x < y: 
    if y % x == 0:
        print('São multiplos')
    else:
        print('Não multiplos')