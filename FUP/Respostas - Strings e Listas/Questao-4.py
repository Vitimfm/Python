def contaVogais(s):
    qtd = 0
    vogais = 'aeiou'
    for i in s.lower():
        if i in vogais:
            qtd += 1
    return qtd