def inverte(s):
    nomeInv = ''
    for i in s:
        nomeInv = i + nomeInv
    return nomeInv

x = input('Digite: ')
print(inverte(x))

    