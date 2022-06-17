n = int(input('Entre com um numero: '))
print('=============')
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
print('=============')
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
print('=============')
for i in range(1, n + 1):
    for j in range(i):
        print(' ', end='')
    print('*')
print('=============')
for i in range(n, 0, -1):
    for j in range(i):
        print(' ', end='')
    print('*')
print('=============')
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
print('=============')
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
print('==============')
for i in range(n, 0, -1):
    for j in range(n - i):
       print(' ', end='')
    for j in range(n):
        print('* ', end='')
    print()
print('==============')
for i in range(n, 0, -1):
    for j in range(n - i):
       print(' ', end='')
    for j in range(i):
        print('* ', end='')
    print()
print('==============')
for i in range(n, 0, -1):
  for _ in range(n - i):
    print(' ', end='')
  for c in range(i):
    if c == 0 or c + 1 == i:
      print('* ', end='')
    else:
      print('  ', end='')
  print()
