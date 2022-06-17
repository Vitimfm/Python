'''
def removeStrings(s, p):
    res = ''
    for i in s.lower():
        if i not in p:
            res += i
    return res
'''

def removePedaco(s, p):
    return ''.join(s.split(p))
    
x = str(input('Digite: '))
y = str(input('Remove: '))

print(removePedaco(x, y))
