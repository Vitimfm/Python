try:
    sal = float(input('Digite o salario da pessoa: '))
    if 0 <= sal <= 1000:
        print('Porcentagem: 20%')
        novo_sal = (sal * (20 / 100)) + sal
        aumento = novo_sal - sal 
        print(f'Novo salário: {novo_sal:.2f} \nAumento: {aumento:.2f}')   
    elif 1001 <= sal <= 3000: 
        print('Porcentagem: 15%')
        novo_sal = (sal * (15 / 100)) + sal
        aumento = novo_sal - sal 
        print(f'Novo salário: {novo_sal:.2f} \nAumento: {aumento:.2f}')   
    elif 3001 <= sal <= 8000: 
        print('Porcentagem: 10%')
        novo_sal = (sal * (10 / 100)) + sal
        aumento = novo_sal - sal 
        print(f'Novo salário: {novo_sal:.2f} \nAumento: {aumento:.2f}')   
    elif sal > 8001: 
        print('Porcentagem: 5%')
        novo_sal = (sal * (5 / 100)) + sal
        aumento = novo_sal - sal 
        print(f'Novo salário: {novo_sal:.2f} \nAumento: {aumento:.2f}')   
    else:
        print('Salário Inválido')
except:
    print('Entre com um valor de salário válido.')

    