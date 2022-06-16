n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
final = n1 + n2 
if final >= 60.0:
    print(f'Nota final: {final}', '\nAprovado')
else:
    print(f'Nota final: {final}', '\nReprovado')