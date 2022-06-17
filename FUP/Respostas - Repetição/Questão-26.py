import turtle
n = int(input('Digite o numeros de quadrados: '))
main = turtle.Screen()
main.setup(800, 600)

caneta = turtle.Turtle()
caneta.shape('arrow')
caneta.speed(5)
for _ in range(n):
    for i in range(2):
        caneta.forward(50)
        caneta.left(90)
        caneta.forward(50)
        caneta.left(90)
    caneta.forward(50)

while True:
    main.update()