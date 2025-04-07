import turtle
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360.0 / n  # ponto flutuante para evitar erros com divisão inteira
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#Criando o turtle
bob = turtle.Turtle()

polygon(t=bob, n=5, length=80)  # pentágono

turtle.mainloop()

