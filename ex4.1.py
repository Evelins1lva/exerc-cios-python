import turtle

# Cria um objeto Turtle chamado bob
bob = turtle.Turtle()
print(bob)

# Fazer o turtle se mover e desenhar um ângulo reto
bob.fd(100)     # 100 pixels
bob.lt(90)      # 90 graus para a esquerda
bob.fd(100)     # Avança mais 100 pixels

turtle.mainloop()