from turtle import Turtle

t = Turtle()
t.speed(0)
t.width(3)
t.turtlesize(1.5)

t.up()
t.bk(150)
t.down()
t.begin_fill()
for _ in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(120)
    t.lt(90)
t.end_fill()

t.up()
t.lt(90)
t.fd(20)
t.rt(90)

colors = {
    0: 'red',
    1: 'yellow',
    2: 'green',
}
distances = {
    0: 60,
    1: 90,
    2: 90,
}
for i in range(3):
    t.fd(distances.get(i))
    t.down()
    t.color(colors.get(i))
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.up()

t.ht()
t.screen.mainloop()