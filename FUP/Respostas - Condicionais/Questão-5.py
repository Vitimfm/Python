print('Digite notas entre 0 e 10 para o cálculo da média.')

nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
nota3 = float(input('Digite o valor da terceira nota: '))
media = (nota1 + nota2 + nota3)/3

if nota1 >= 0 and nota1 <= 10:
    if nota2 >= 0 and nota2 <= 10:
        if nota3 >= 0 and nota3 <= 10:
            print(f'A média das notas é {media:.2f}')
            if media >= 7:
                print('Aluno Aprovado.')
            elif media >= 4 and media < 7:
                print('Aluno de Recuperação')
            else:
                print('Aluno Reprovado')
        else:
            print("A terceira nota não está entre 0 e 10")
    else:
     print("A segunda nota não está entre 0 e 10")
else:
    print("A primeira nota não está entre 0 e 10")