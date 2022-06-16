horario = input('Digite um horario entre 0-24: ')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 24:
        print('Digite um horário válido')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('boa tarde')
        else:
            print('Boa noite')
else:
    print('escreva um horario válido')