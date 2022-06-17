dia = int(input('Digite o dia do seu aniversário: '))
print('jan  fev  mar  abr')
print('mai  jun  jul  ago')
print('set  out  nov  dez')
mes = str(input('Digite o mês do seu aniversário: '))

if dia >= 1 and dia <=10:
    nome = ' de frag negativo'
elif dia > 10 and dia <= 20:
    nome = 'camper'
else:
    nome = 'que só morre'

if mes == 'jan':
    print('Mago',nome)
elif mes == 'fev':
    print('Arqueiro',nome)
elif mes == 'mar':
    print('Suporte',nome)
elif mes == 'abr':
    print('Bardo',nome)
elif mes == 'mai':
    print('Sniper',nome)
elif mes == 'jun':
    print('Guerreiro',nome)
elif mes == 'jul':
    print('Fuzileiro',nome)
elif mes == 'ago':
    print('Mvp',nome)
elif mes == 'set':
    print('Barbaro',nome)
elif mes == 'out':
    print('NPC',nome)
elif mes == 'nov':
    print('PK',nome)
else:
    print('Noob',nome)







