import turtle
import time
import random

# Configuração da tela
wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("black")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("square")
comida.color("red")
comida.penup()
comida.goto(0, 100)

segmentos_cobra = []

# Funções
def move():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)

    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)

    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)

    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

def vai_para_cima():
    if cabeca.direction != "down":
        cabeca.direction = "up"

def vai_para_baixo():
    if cabeca.direction != "up":
        cabeca.direction = "down"

def vai_para_esquerda():
    if cabeca.direction != "right":
        cabeca.direction = "left"

def vai_para_direita():
    if cabeca.direction != "left":
        cabeca.direction = "right"

# Teclado
wn.listen()
wn.onkeypress(vai_para_cima, "w")
wn.onkeypress(vai_para_baixo, "s")
wn.onkeypress(vai_para_esquerda, "a")
wn.onkeypress(vai_para_direita, "d")

# Loop principal do jogo
while True:
    wn.update()

    # Verifica colisão com a borda da tela
    if (
        cabeca.xcor() > 290
        or cabeca.xcor() < -290
        or cabeca.ycor() > 290
        or cabeca.ycor() < -290
    ):
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"

        # Esconder os segmentos da cobra
        for segmento in segmentos_cobra:
            segmento.goto(1000, 1000)

        segmentos_cobra.clear()

    # Verifica colisão com a comida
    if cabeca.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("grey")
        novo_segmento.penup()
        segmentos_cobra.append(novo_segmento)

    # Move os segmentos da cobra
    total_segmentos = len(segmentos_cobra)
    for index in range(total_segmentos - 1, 0, -1):
        x = segmentos_cobra[index - 1].xcor()
        y = segmentos_cobra[index - 1].ycor()
        segmentos_cobra[index].goto(x, y)

    if total_segmentos > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos_cobra[0].goto(x, y)

    move()

    # Verifica colisão com o próprio corpo
    for segmento in segmentos_cobra:
        if segmento.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0, 0)
            cabeca.direction = "stop"

            for segmento in segmentos_cobra:
                segmento.goto(1000, 1000)

            segmentos_cobra.clear()

    time.sleep(0.1)
