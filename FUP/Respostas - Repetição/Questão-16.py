n = int(input('Digite um numero: '))
count = 1
for i in range (1, n+1):
    for _ in range(i):
        print(count, end=' ')
        count += 1
    print() 