n = int(input('Digite a quantidade de pontos: '))
xmin = 0
xmax = 0
ymin = 0
ymin = 0
for i in range(1, n + 1):
    x = int(input(f'Digite a {i}º coordena de X: '))
    y = int(input(f'Digite a {i}º coordena de Y: '))
    
    
    if i == 1:
        xmax = xmin = x
        ymax = ymin = x
    else: 
        if x > xmax:
            xmax = x
        elif x < xmin:
            xmin = x
            
        if y > ymax:
            ymax = y
        elif y < ymin:
            ymin = y
     
print(f'Ponto Mínimo: ({xmin},{ymin})')
print(f'Ponto Máximo: ({xmax},{ymax})')
            
            

 