c1 = [1,3,5,7,9,11]
c2 = [8,9,10,11,12]


def uniao(c1, c2):
    c3 = c1 + c2
    l = c3[:]
    for i in range(len(c3)):
        if c3.index(c3[i]) != i:
            l.remove(c3[i])
    return l 

print(uniao(c1, c2))


def intersecao(c1, c2):
    c3 = c1 + c2
    l = c3[:]
    for i in range(len(c3)):
        if c3.index(c3[i]) == i:
            l.remove(c3[i])
    return l 

print(intersecao(c1, c2))

def diferenca(c1, c2):
    lis = []
    for i in c1:
        if i not in c2:
            lis.append(i)
    return lis

print(diferenca(c1, c2))
            
    