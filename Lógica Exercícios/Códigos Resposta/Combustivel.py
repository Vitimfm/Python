alc = 0
gaso = 0
die = 0
while True:
    try: 
        x = int(input('Escolha uma das opções:\n[1] Alcool\n[2] Gasolina\n[3] Diesel\n[4] Sair\nSua escolha: '))
        if x == 1:
            alc += 1
        elif x == 2:
            gaso += 1
        elif x == 3:
            die += 1
        elif x == 4:
            print('Muito Obrigado')
            print(f'[1] Alcool: {alc}\n[2] Gasolina: {gaso}\n[3] Diesel: {die}')
            break
        else:
            continue
    except:
        print('Digite apenas números')