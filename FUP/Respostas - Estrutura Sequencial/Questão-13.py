altura = float(input('Digite a altura do cilindro circular reto: '))
raioB = float(input('Digite o raio da base do cilindro circular reto: '))

pi = 3.14

areaL = 2 * pi * raioB * altura
areaB = pi * raioB**2
volume = areaB * altura

print(f'A área lateral é igual a {areaL}')
print(f'A área da base é igual a {areaB}')
print(f'O volume é igual a {volume}')

