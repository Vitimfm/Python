n = int(input('Quantas pessoas serão digitadas: '))

nomes = []
alturas = []
idades = []

for i in range(1, n + 1):
    print(f'Dados da {i}º pessoa: ')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    nomes.append(nome)
    alturas.append(altura)
    idades.append(idade)

count = 0
somaAlt = 0
  
for i in alturas:
    somaAlt += i
    count += 1
media = somaAlt / count
print(f'Altura média: {media:.2f}')

count16 = 0
for i in range(n):
    if idades[i] < 16:
        count16 += 1

perAlt16 = (count16 * 100) / count
print(f'Pessoas com menos de 16 anos: {perAlt16:.2f}%') 

for i in range(n):
    if idades[i] < 16:
        print(nomes[i])


    