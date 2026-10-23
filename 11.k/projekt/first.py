import turtle

ablak = turtle.Screen()
ablak.setup(600, 600)
ablak.bgcolor("lightgreen")

t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.goto(-250, -250)
t.speed(0)

teki = turtle.Turtle()
teki.shape("turtle")
teki.color("red")
teki.goto(250, 250)


def teki_fel():
    y = teki.ycor()
    teki.sety(y + 10)


def teki_le():
    y = teki.ycor()
    teki.sety(y - 10)


def teki_balra():
    x = teki.xcor()
    teki.setx(x - 10)


def teki_jobra():
    x = teki.xcor()
    teki.setx(x + 10)


def tavolsag(ax, bx, ay, by):
    t = ((bx - ax)**2 + (by - ay)**2)**0.5
    return t


dx = 3
dy = 1

ablak.listen()
ablak.onkeypress(teki_fel, "Up")
ablak.onkeypress(teki_le, "Down")
ablak.onkeypress(teki_balra, "Left")
ablak.onkeypress(teki_jobra, "Right")

while True:
    tav = tavolsag(t.xcor(), t.ycor(), teki.xcor(), teki.ycor())
    if tav < 30:
        teki.color("yellow")
    else:
        teki.color("red")

    x = t.xcor()
    y = t.ycor()
    t.setx(x + dx)
    t.sety(y + dy)

    if t.xcor() > 300:
        dx = -dx
    if t.xcor() < -300:
        dx = -dx
    if t.ycor() > 300:
        dy = -dy
    if t.ycor() < -300:
        dy = -dy
