import turtle
import colorsys
t = turtle.Turtle()
homes=turtle.Screen().bgcolor('black')
t.speed(0)

h=0
n=70
for i in range(360):
    c=colorsys.hsv_to_rgb(h, 1, 0.8)
    h+=1/n
    t.color(c)

    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(2 * i)

turtle.exitonclick()