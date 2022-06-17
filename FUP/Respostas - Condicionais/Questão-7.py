carac = str(input('Digite um caractere: '))
if carac.isdigit():
    print('numero')
elif carac == 'a' or carac == 'e' or carac == 'i' or carac == 'o' or carac == 'u':
    print('vogal')
else:
        print('consoante')
#Como analisar apenas um caracter e limitar o usuario de escreve uma string?