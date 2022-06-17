def palindromo(s):
    nomeInv = ''
    for i in s:
        nomeInv = i + nomeInv
    if nomeInv == s:
        return True
    return False

x = str(input('Digite um palavra: '))
print(palindromo(x))
    