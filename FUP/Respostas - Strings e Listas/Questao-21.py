nome= 'Vitor Freitas Meneses'
partes = nome.split(' ')

newPartes = []
for i in partes[0: -1]:
    newPartes.append(i[0] + '.')

print(partes[-1] + ', ' + ' '.join(newPartes))



'''
nome= 'Vitor Freitas Meneses'
x = nome.split(' ')
print(x[0: -1])
'''