gli = float(input('Digite o valor da glicose: '))

if 0 <= gli <= 100: 
    print('Normal')
elif 101 <= gli <= 140: 
    print('Elevado')
elif gli < 0:
    print('Glicose Inválida')
else:
    print('Diabetes')

    