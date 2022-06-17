ini = int(input('Digite a hora inicial: '))
fim = int(input('Digite a hora final: '))

if fim > ini:
    duracao = fim - ini
    print(f'Duração do jogo: {duracao} hora(s)')
else:
    duracao = (ini - 24) * -1  + fim
    print(f'Duração do jogo: {duracao} hora(s) ')

