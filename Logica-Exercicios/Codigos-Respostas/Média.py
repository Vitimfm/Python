armazena = 0
idades = 0
cont = 0

while idades >= 0:
    idades = int(input('Digite uma idade: '))
    
    if cont == 0 and idades < 0: 
        print('Impossivel Calcular')
        break
    if idades < 0:
        media = armazena / cont
        print(f'Média das idades válidas: {media:.2f}')
    else:
        armazena += idades
        cont += 1 

    
    
        
        
    