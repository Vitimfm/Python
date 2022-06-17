import turtle

lado = int(input('Tamanho do lado: '))
li = int(input('Quantidade de linhas: '))
col = int(input('Quantidade de colunas: '))

main = turtle.Screen()
main.bgcolor('lightgray')
caneta = turtle.Turtle()
caneta.speed(0)
caneta.up()
caneta.goto(-200, 200)
caneta.down()

for c in range(li):
    for i in range(col):
        if i % 2 == 0:
            caneta.color('black')
        else:
            caneta.color('white')
        caneta.begin_fill()

        for _ in range(4):
            caneta.forward(lado)
            caneta.right(90)
        caneta.end_fill()
        caneta.forward(lado)

    if c % 2 == 0:
        caneta.right(90)
        caneta.forward(lado * 2)
        caneta.right(90)
    else:
        caneta.left(180)

while True:
    main.update()