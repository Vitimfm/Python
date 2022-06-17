nota = float(input('Digite sua nota: '))

if nota < 0 or nota > 10:
    print('Nota Invalida')
elif nota >= 0 and nota <= 5:
    print('Conceito E')
elif nota > 5 and nota <= 6:
    print('Conceito D')
elif nota > 6 and nota <= 7:
    print('Conceito C')
elif nota > 7 and nota <= 8:
    print('Conceito B')
else:
    print('Conceito A')




