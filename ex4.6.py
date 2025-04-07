import turtle
import math

# Função que desenha um polígono regular
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

# Função que desenha um círculo aproximado com raio r
def circle(t, r):
    circumference = 2 * math.pi * r         
    n = int(circumference / 3) + 1          
    length = circumference / n              
    polygon(t, n, length)                   

# Criação do turtle
bob = turtle.Turtle()

# Chamada da função
circle(bob, 100)  

turtle.mainloop()
