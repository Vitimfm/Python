import turtle
n = int(input('Quantidade de lados do polígono: '))
lado = int(input('Tamanho do lado: '))
main = turtle.Screen()
caneta = turtle.Turtle()

for _ in range(n):
    caneta.forward(lado)
    caneta.right(360 / n)

while True:
    main.update()
