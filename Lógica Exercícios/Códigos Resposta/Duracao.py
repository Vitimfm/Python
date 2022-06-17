seg = int(input('Digite o valor em segundos: '))
horas = seg // 3600
min = (seg % 3600) // 60
segundos = (seg % 3600) % 60
print(f'[{horas}:{min}:{segundos}]')
