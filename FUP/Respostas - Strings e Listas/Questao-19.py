l1 = [1, 1, 2, 3, 5, 7, 7, 9, 'oi', 'oi', 9.0, 9.0]


def removeRepetidas(l):
    lis = l[:]
    for i in range(len(l)):
        if l.index(l[i]) != i:
            lis.remove(l[i])
                 
    return lis

print(removeRepetidas(l1))
                