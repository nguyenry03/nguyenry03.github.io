import turtle
from Shapes import *




ryan = turtle.Turtle('turtle')

wn = turtle.Screen()
wn.colormode (255)
wn.bgcolor (0, 0, 0)







ryan.color(0, 255, 0)
ryan.speed(9)


def strawberry(peach, sidelength, n):
    for i in range (n):
        peach.forward(sidelength)
        peach.right(360/n)



r = 15
g = 20
b = 225

for i in range (100,1,-1):
    ryan.color(r,g,b)
    strawberry(ryan, i, 4)
    r = r+2
    g = g+2
    b = b-2








    
