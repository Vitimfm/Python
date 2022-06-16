try: 
    n = int(input('Insira a quantidade de notas: '))
    pond = 0
    di = 0
    for i in range(1, n + 1):
        x = float(input(f'Informe a {i}º nota: '))
        b = float(input(f'Informe o peso da {i}º nota: '))
        pond += x * b
        di += b
        media = pond / di
    print(f'Média ponderada: {media:.1f}') 
except:
    print('Insira uma nota válida.')      