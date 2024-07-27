import turtle
import random

# Configurações da tela
screen = turtle.Screen()
screen.title("Desenho de Linhas em Vários Sentidos ao Redor de um Círculo")
screen.bgcolor("white")

# Configurações da tartaruga (turtle)
t = turtle.Turtle()
t.speed(0)  # Define a velocidade da tartaruga no máximo

# Desenha um círculo
radius = 100
t.penup()
t.goto(0, -radius)  # Move a tartaruga para a posição inferior do círculo
t.pendown()
t.circle(radius)  # Desenha o círculo

# Função para desenhar linhas ao redor do círculo
def desenhar_linhas_ao_redor_do_circulo(num_linhas, radius):
    for _ in range(num_linhas):
        t.penup()
        angle = random.randint(0, 360)  # Define um ângulo aleatório ao redor do círculo
        t.setheading(angle)
        t.goto(radius * turtle.cos(turtle.radians(angle)), radius * turtle.sin(turtle.radians(angle)))  # Move para a circunferência do círculo
        t.pendown()
        length = random.randint(50, 150)  # Define um comprimento aleatório
        t.forward(length)

# Chama a função para desenhar 50 linhas ao redor do círculo
desenhar_linhas_ao_redor_do_circulo(50, radius)

# Finaliza o desenho
turtle.done()
