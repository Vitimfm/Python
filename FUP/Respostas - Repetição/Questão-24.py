ax = int(input('Digite a coordenada x: '))
ay = int(input('Digite a coordenada y: '))

bx = int(input('Digite um deslocamento para x: '))
by = int(input('Digite um deslocamento para y: '))

n = int(input('Digite o numero de pontos: '))

for i in range(1, n + 1):
    ax += bx 
    ay += by
    print(f'Ponto({i}): [{ax},{ay}]')


    
    