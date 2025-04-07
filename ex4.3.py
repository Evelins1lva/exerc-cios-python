import turtle
import math

bob = turtle.Turtle()

#  Desenhar um quadrado
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# Versão do square com tamanho dos lados
def square_length(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

# Desenhar um polígono regular com n lados
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# Desenhar um círculo aproximado com raio r
def circle(t, r):
    circ = 2 * math.pi * r
    steps = 50
    length = circ / steps
    polygon(t, steps, length)

# Desenha um arco com raio r e ângulo em graus
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    steps = 50
    step_length = arc_length / steps
    step_angle = angle / steps

    for i in range(steps):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 100, 180)

turtle.mainloop()

