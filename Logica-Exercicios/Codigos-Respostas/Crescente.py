
while True:
    x = y = ''
    try:
        x = float(input('Digite um valor x: '))
        y = float(input('Digite um valor y: '))
        
        if y > x:
            print('Crescente')
        elif x == y:
            print('Numeros Iguais!')
            break
        else:
            print('Decresente')
    except:
        print('Coloque apenas números')