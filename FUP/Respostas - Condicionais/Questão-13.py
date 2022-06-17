produto = input('Digite o nome do produto: ')
massa_p1 = float(input('Digite a primeira massa do produto: '))
preco_p1 = float(input('Digite o preço do produto: '))
massa_p2 = float(input('Digite a segunda massa do produto: '))
preco_p2 = float(input('Digite o preço do produto: '))

if massa_p1 / preco_p1 > massa_p2 / preco_p2:
    print(f'O {produto} de {massa_p1}g por R$ {preco_p1:.2f} é mais vantajoso.')
else:
    print(f'O {produto} de {massa_p2}g por R$ {preco_p2:.2f} é mais vantajoso.')