'''
Conversão Temperatura.
'''
temp = str(input('Digite "C" para [C em F] ou \nDigite "F" para [F em C]: '))

if temp.lower() == 'c':
    print('Opção: Celsius.')
    cel = float(input('Digite a temperatura em Celsius: '))
    celFar = 1.8*cel + 32
    print(f'{cel}º Celsius equivalem à {celFar:.2f} Fahrenheit.')
    
elif temp.lower() == 'f':
    print('Opção: Fahrenheit.')
    far = float(input('Digite a temperatura em Fahrenheit: '))
    farCel = (far-32) / 1.8
    print(f'{far} Fahrenheit equivalem à {farCel:.2f}º Celsius.')
    
else:
    print('Opção Inválida')
    
    
    
    