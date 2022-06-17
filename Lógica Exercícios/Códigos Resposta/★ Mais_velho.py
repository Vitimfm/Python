n = int(input('Quantidade de pessoas: '))
nome = []
idade = []

for i in range(1, n + 1):
    print(f'Dados da {i}º pessoa.')
    no = str(input('Nome: '))
    ida = int(input('Idade: '))
    nome.append(no)
    idade.append(ida)

max = idade[0]
posMaior = 0
for i in range(n):
    if idade[i] > max:
        max = idade[i]
        posMaior = i

print(f'A pessoa mais velha é: {nome[posMaior]}')

        

      


