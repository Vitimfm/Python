minha_lista = [76, 92.3, 'oi', True, 4, 76]
minha_lista += ['Pêra', 76]
minha_lista.insert(2, 'gato')
minha_lista.insert(0, 99)
minha_lista.remove(76)
minha_lista.pop(minha_lista.index(4))
print(minha_lista)
print(minha_lista.index('oi'))
print(minha_lista.count(76))