'''
Projeto FUP - Jogo com Colisão (CC)
- Vitor Freitas de Meneses 538057 
Sprite 'Link' by 'xander@tsgk.capitainn.net' 
Sprite 'inimigo' by 'zeldapunkgrrl' on Zelda Fan Game Central
Background Sprites: OOT 2D by CheerfulSage & GodsTurf
'''
import turtle
import random

main = turtle.Screen()                  # Abre janela
main.tracer(0)                          # Atualização da tela em tempo mínimo 
main.title('Zeldinha')                  # Titulo do Jogo
main.setup(800, 600)                     # Resolução da janela criada
main.bgpic('background.gif')            # Foto escolhida para plano de fundo
main.bgcolor('lightgreen')              # Cor do plano de Fundo

main.addshape('LinkUp.gif')             # Sprite do personagem para cima
main.addshape('LinkLeft.gif')           # Sprite do personagem para esquerda
main.addshape('LinkRight.gif')          # Sprite do personagem para direita
main.addshape('LinkDown.gif')           # Sprite do personagem para baixo
main.addshape('inimigo.gif')            # Sprite do inimigo
main.addshape('Rupee.gif')              # Sprite do Rupee que será a pontuação 
main.addshape('coracao.gif')            # Sprite do coração para vidas

x = 310          # Variável para cordenada x
y = 215          # Variável para cordenada y
vidas = 3        # Variável para vidas
placar = 0       # Variável para placar começando em 0
recorde = 0
FPS =30         # Variável para os frames na função ontimer

# Desenhar Arena Retangular

arena = turtle.Turtle()          # definindo 'arena' como um turtle
def desenhaArena():              # Definindo a função
    arena.penup()                # Para não riscar na trajetória feita
    arena.speed(0)               # Define velocidade do turtle 'arena'    
    arena.pensize(width=4)       # Define largura da caneta
    arena.goto(-340, -250)       # Começa desenhando na parte inferior esquerda da arena
    arena.pendown()              # Para riscar na trajetória feita
    arena.color('black')         # Cor da caneta
desenhaArena()            

for i in range(2):               # Repete a sequencia abaixo duas vezes para fechar a arena
    arena.forward(680)           # Anda para frente até o ponto definido
    arena.left(90)               # Vira para esquerda em 90 graus
    arena.forward(500)           # Anda para frente até o ponto definido
    arena.left(90)               # Vira para esquerda em 90 graus
arena.hideturtle()               # Esconde o turtle 'arena'

# Definir Vida, Pessonagem, Inimigo, Rupee e Pontuação e Recorde  

coracao1 = turtle.Turtle()
coracao1.penup()
coracao1.speed(0)
coracao1.goto(-325, 270)          # Vai imediatamente para o ponto definido
coracao1.shape('coracao.gif')     # Coloca o sprite de coração

coracao2 = turtle.Turtle()
coracao2.penup()
coracao2.speed(0)
coracao2.goto(-300, 270)
coracao2.shape('coracao.gif')

coracao3 = turtle.Turtle()
coracao3.penup()
coracao3.speed(0)
coracao3.goto(-275, 270)
coracao3.shape('coracao.gif')

persona_1 = turtle.Turtle()
persona_1.speed(0)
persona_1.shape('LinkDown.gif')
persona_1.penup()
persona_1.goto(0, 0)              # Jogador começa nesse ponto
persona_1.veloc = 15              # Definindo velocidade para persona_1

inimigo = turtle.Turtle()
inimigo.speed(0)
inimigo.shape('inimigo.gif')
inimigo.penup()
inimigo.goto(random.randint(-340, 340),random.randint(-250, 250))   # Inimigo começa posição aleatória
inimigo.veloc = 5      # Definindo velocidade para inimigo

rupee = turtle.Turtle()
rupee.speed(0)
rupee.shape('Rupee.gif')
rupee.penup()
rupee.goto(random.randint(-340, 340),random.randint(-250, 250))    # Rupee começar posição aleatória
rupee.veloc = 4        # Definindo Velocidade para Rupee

pontuacao = turtle.Turtle()
pontuacao.speed(0)
pontuacao.color('black') 
pontuacao.penup()
pontuacao.hideturtle()
pontuacao.goto(315, 260)
pontuacao.write('0', font=('Verdana', 14, 'bold'))            # Para escrever na tela a pontuação

rupee_placar = turtle.Turtle()         
rupee_placar.speed(0)
rupee_placar.shape('Rupee.gif')
rupee_placar.penup()
rupee_placar.goto(300, 275)

recor = turtle.Turtle()
recor.speed(0)
recor.color('black') 
recor.hideturtle()
recor.penup()
recor.goto(0, 260)
recor.write('recorde: 0', font=('Verdana', 14, 'bold'), align='center')    # Escrever o recorde

# Funções limites do Personagem na arena definindo movimentação 

def persona_1_up():
    persona_1.shape('LinkUp.gif')             # Define o sprite na posição escolhida 
    persona_1.setheading(90)                  # setheading define para onde o 'persona_1' está virado
    if persona_1.ycor() < y:                  # Checa ponto y do persona_1
        persona_1.forward(persona_1.veloc)    # condição de andar para frente na velocidade definida
persona_1_up()
def persona_1_right():
    persona_1.shape('LinkRight.gif')
    persona_1.setheading(0)
    if persona_1.xcor() < x:
        persona_1.forward(persona_1.veloc)
persona_1_right()
def persona_1_left():
    persona_1.shape('LinkLeft.gif')
    persona_1.setheading(180)
    if persona_1.xcor() > -x:
        persona_1.forward(persona_1.veloc)
persona_1_left()
def persona_1_down():
    persona_1.shape('LinkDown.gif')
    persona_1.setheading(270)
    if persona_1.ycor() > -y:
        persona_1.forward(persona_1.veloc)
persona_1_down()


# Listen para Movimentação no teclado

main.listen()
main.onkeypress(persona_1_up,'Up')
main.onkeypress(persona_1_down,'Down')
main.onkeypress(persona_1_right,'Right')
main.onkeypress(persona_1_left,'Left')
                             
# Função updateScreen para atualização da tela

def updateScreen():
    
    # Movimento e Limite do inimigo

    inimigo.forward(inimigo.veloc)
    if inimigo.ycor() > 220:
        inimigo.sety(220)
        inimigo.setheading(random.randint(0, 360))
    if inimigo.ycor() < -220:
        inimigo.sety(-220)
        inimigo.setheading(random.randint(0, 360))
    if inimigo.xcor() > 310:
        inimigo.setx(310)
        inimigo.setheading(random.randint(0, 360))
    if inimigo.xcor() < -305:
        inimigo.setx(-305)
        inimigo.setheading(random.randint(0, 360))

    # Movimento e Limite do rupee

    rupee.forward(rupee.veloc)
    if rupee.ycor() > 230:
        rupee.sety(230)
        rupee.setheading(random.randint(0, 360))
    if rupee.ycor() < -230:
        rupee.sety(-230)
        rupee.setheading(random.randint(0, 360))
    if rupee.xcor() > 325:
        rupee.setx(325)
        rupee.setheading(random.randint(0, 360))
    if rupee.xcor() < -325:
        rupee.setx(-325)
        rupee.setheading(random.randint(0, 360))
        
    # Colisão Inimigo
        
    def colisaoInimigo():
        global vidas
        global placar 
        global recorde  
        if inimigo.xcor() + 20 >= persona_1.xcor() - 20 and inimigo.xcor() -20 <= persona_1.xcor() + 20 and inimigo.ycor() + 25 >= persona_1.ycor() -25 and inimigo.ycor() - 25 <= persona_1.ycor() + 25:
            inimigo.goto(random.randint(-340, 340),random.randint(-250, 250))   # Define um ponto random para ir após a colisão
            inimigo.setheading(random.randint(0, 360))                     # Define uma direção random após a colisão
            vidas -= 1                      # Perde uma vida após colisão
            if vidas == 2:
                coracao3.hideturtle()       # Some um coração
            elif vidas == 1:
                coracao2.hideturtle()       # Some mais um coração
            else:
                coracao1.hideturtle()       # Some o último coração 
                vidas = 3                   # Vida volta ter 3 corações que serão mostrados novamente
                coracao3.showturtle()
                coracao2.showturtle()
                coracao1.showturtle()
                persona_1.goto(0,0)        # Após perder todas as vidas e restaura-las, jogador vai para o centro do jogo
                if placar > recorde:
                    recorde = placar
                    recor.clear()
                    recor.write('recorde: {}'.format(recorde), font=('Verdana', 15, 'bold'), align='center')
                # Resetar Placar:
                pontuacao.clear()     
                placar = 0
                pontuacao.write('{}'.format(placar), font=('Verdana', 15, 'bold'))
    colisaoInimigo() 
    
    # Colisão Rupee
    
    def colisaoRupee():
        global placar
        global pontuacao
        if rupee.xcor() + 20 >= persona_1.xcor() - 20 and rupee.xcor() -20 <= persona_1.xcor() + 20 and rupee.ycor() + 25 >= persona_1.ycor() - 25 and rupee.ycor() -25 <= persona_1.ycor() + 25:
            rupee.goto(random.randint(-340, 340),random.randint(-250, 250))  # Define um ponto random para ir após a colisão
            rupee.setheading(random.randint(0, 360))                    # Define uma direção random após a colisão
            placar += 1           # Após colisão, placar soma 1
            pontuacao.clear()     # Limpa pontuação anterior
            pontuacao.write('{}'.format(placar), font=('Verdana', 14, 'bold'))   # Reescreve o placar 
    colisaoRupee()
    
    turtle.ontimer(updateScreen, 1000 // 50)        # Para atualização em tempo real da tela

updateScreen()

while True:
    main.update()