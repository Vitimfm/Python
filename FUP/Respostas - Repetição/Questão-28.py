import turtle
camadas = int(input('Digite o numero de camadas: '))
altura = int(input('Digite a altura: '))
largura = int(input('Digite a largura: '))

main = turtle.Screen()
main.setup(800, 600)

caneta = turtle.Turtle()
caneta.shape('arrow')
caneta.speed(5)

for i in range(1, camadas + 1):
    for _ in range(2):
        caneta.forward(largura * i)
        caneta.right(90)
        caneta.forward(altura)
        caneta.right(90)
    caneta.right(90)
    caneta.forward(altura)
    caneta.left(90)

while True:
    main.update()