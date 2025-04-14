import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner 

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.hypot(dx, dy)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    
    pontos = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height),
    ]
    return all(point_in_circle(circle, p) for p in pontos)

def rect_circle_overlap(circle, rect):
    pontos = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height),
    ]
    return any(point_in_circle(circle, p) for p in pontos)
