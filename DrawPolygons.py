import turtle


print ('Hello! Want me to draw a polygon for you?')
print ('How many sides do you want do you want your polygon to be?')
s = int(input())
print ('Now how long do you want the sides to be?')
p = int(input())
turt = turtle.Turtle('turtle')
angle = s -2
angle_1 = angle * 180
real_angle = 180 - (angle_1/s)

wn = turtle.Screen()
wn.colormode(255)
def AnyRegPoly(s,r,g,b):
    for i in range (s):
        turt.forward (p)
        turt.left (real_angle)
        turt.color(r,g,b)
        turt.stamp()
        r = r-7
        g = g+10
        b = b-8


AnyRegPoly(s,255,30,215)
