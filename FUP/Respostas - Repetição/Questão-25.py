'''
[?]
'''

ax = int(input('Coordenada x: '))
ay = int(input('Coordenada y: '))

bx = int(input('Vetor deslocamento para x: '))
by = int(input('Vetor deslocamento para y: '))

xmin = int(input('Xmin da caixa: '))
ymin = int(input('Ymin da caixa: '))

xmax = int(input('Xmax da caixa: '))
ymax = int(input('Xmax da caixa: '))

n = int(input('Numero de pontos: '))

while ax < xmax:
    ax += bx 
    ay += by
    colide = True
    if ax < xmax and ax > xmin and ay < ymax and ay > ymin:
        print('Colide')
        break
    else:
        colide = False

if colide == False:
    print('Não colide')


    