import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)

# Criar a janela e a tartaruga
janela = turtle.Screen()
t = turtle.Turtle()
t.speed("fastest") 

draw(t, length=10, n=5)

janela.mainloop()
