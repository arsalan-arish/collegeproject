from turtle import Turtle

t = Turtle()
t.speed(0)
t.width(3)
t.turtlesize(1.5)

for i in range(1, 11):
    t.circle(i*15)
    t.up()
    t.rt(90)
    t.fd(15)
    t.lt(90)
    t.down()

t.screen.mainloop()