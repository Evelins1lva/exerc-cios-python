import turtle

# Definir uma função para desenhar um quadrado
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

# Criando o primeiro turtle: bob
bob = turtle.Turtle()
square(bob)  

# Criando um segundo turtle: alice
alice = turtle.Turtle()
alice.penup()
alice.goto(-150, 0)  
alice.pendown()
square(alice)  

turtle.mainloop()
