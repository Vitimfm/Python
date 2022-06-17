senha = 2002
while True: 
    tent = ''
    try:  
        tent = int(input('Digite a senha: '))
        if tent != senha:
            print('Senha Incorreta. Tente Novamente.')
            continue
        else: 
            print('Senha Correta. Acesso Permitido')
            break
    except:
        print('Coloque apenas números')
    