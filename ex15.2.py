import turtle

def draw_rect(t, rect):
    """Desenha um retângulo com turtle t e objeto Rectangle."""
    t.penup()
    t.goto(rect.corner.x, rect.corner.y)
    t.pendown()

    for _ in range(2):
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)

def draw_circle(t, circle):
    """Desenha um círculo com turtle t e objeto Circle."""
    t.penup()
    t.goto(circle.center.x, circle.center.y - circle.radius)
    t.setheading(0) 
    t.pendown()
    t.circle(circle.radius)
