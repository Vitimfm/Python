while True:
    try:
        r = float(input('Digite o valor do raio ou "0" para sair: '))
        if r == 0: break
        area = 3.14159 * (r**2)
        print(f'Area do circulo: {area:.3f}')
    except:
        print('Digite valores válidos.')