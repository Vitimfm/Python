l1 = [2, 4, 6, 8, 10]
l2 = [1, 3, 5, 7, 9]

def cobina(l1, l2):
    lis = []
    l3 = l1 + l2
    while len(l3) > 0:
        min = l3[0]
        for i in l3:
            if i < min:
                min = i
        lis.append(min)
        l3.remove(min)    
    return lis

print(cobina(l1,l2))

