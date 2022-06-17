while True: 
    n1 = n2 = ''
    try:
        n1 = float(input('Digite a nota 1: '))
        n2 = float(input('Digite a nota 2: '))
        if 0 <= n1 <= 10 and 0 <= n2 <= 10:
            media = (n1 + n2) / 2
            print(f'A média das notas é: {media}')
            break
        else:
            print('As notas devem está entre 0-10. Tente Novamente.')
    except:
        print('Digite apenas notas válidas.')
            