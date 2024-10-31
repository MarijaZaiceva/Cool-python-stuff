from turtle import *

def gradientSquare():
    colormode(255)
    hideturtle()
    speed(0)

    pensize(10)
    r = 0
    g = 0
    b = 0
    n = 255
    
    for w in range(255):
        for i in range(n):
            pencolor(r, g, b)
            forward(1)
            b = b + 1
        left(90)    
        for i in range(n):
            pencolor(r, g, b)
            forward(1)
            r = r + 1
        left(90)
        for i in range(n):
            pencolor(r, g, b)
            forward(1)
            b = b - 1
        left(90)
        for i in range(n-5):
            pencolor(r, g, b)
            forward(1)
            r = r - 1
        left(90)
        n=n-5
gradientSquare()
