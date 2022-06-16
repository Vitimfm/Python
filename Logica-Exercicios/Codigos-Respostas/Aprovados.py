n = int(input('Quantos alunos serão digitados: '))

nomes = []
notas1 = []
notas2 = []

for i in range(1, n + 1):
    print(f'Digite os dados do {i}º aluno. ')
    nome = str(input('Nome: '))
    n1 = float(input('1º nota: '))
    n2 = float(input('2º nota: '))
    nomes.append(nome)
    notas1.append(n1)
    notas2.append(n2)

print('Alunos Aprovados:')

soma = 0

for i in range(n):
    soma = (notas2[i] + notas1[i])
    media = soma / 2
    if media >= 6:
        print(nomes[i])
    


        


    
    
    