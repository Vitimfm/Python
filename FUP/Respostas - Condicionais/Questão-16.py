salabase = float(input('Digite o salário-base: '))
depen = int(input('Digite o numero de dependentes: '))

salabruto = salabase + (depen * 120)

if salabruto < 1000:
    IRRF = 0
    print('Isento de IRRF')
elif salabruto >= 1000 and salabruto < 2500:
    IRRF = salabruto * 10 / 100
    print(f'IRRF de 10% = R$ {IRRF}')
else:
    IRRF = salabruto * 20 / 100
    print(f'IRRF de 20% = R$ {IRRF}')

salaliq = salabruto - IRRF

if salaliq < 1750:
    print('Gratificação de R$ 500')
    salareceber = salaliq + 500
else:
    print('Gratificação de R$ 500')
    salareceber = salaliq + 250

print(f'O salário a receber é de R$ {salareceber}.')


