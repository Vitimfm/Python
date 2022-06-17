def repeteVogais(s):
    q = ''
    vogais = 'aeiou'
    for i in s.lower():
        if i in vogais:
            i += i
            q += i
        else:
            q += i
    return q

x = str(input('Digite: '))

print(repeteVogais(x))