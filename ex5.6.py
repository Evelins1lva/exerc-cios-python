import turtle

def koch(t, length):
    if length < 3:
        t.forward(length)
    else:
        length /= 3.0
        koch(t, length)
        t.left(60)
        koch(t, length)
        t.right(120)
        koch(t, length)
        t.left(60)
        koch(t, length)

def snowflake(t, length, depth=3):
    for _ in range(3):
        koch(t, length)
        t.right(120)

# Criando a tartaruga e a janela
janela = turtle.Screen()
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.goto(-150, 90)
t.pendown()

# Desenhar o floco de neve 
snowflake(t, length=300)

janela.mainloop()
