"""In my program I want to draw a Turtle in the nightime with stars in the sky using the Turtle package."""
 
__author__ = "730665579"
 
from turtle import Turtle, done
t: Turtle = Turtle()


def backround() -> None:
    """Makes balck square and fills it in as black for the future stars."""
    t.begin_fill()
    t.goto(-350, 0)
    i: int = 0
    t.left(90)
    t.forward(300)
    while i < 5:
        t.right(90)
        t.forward(800)
        i += 1
    t.end_fill()


def star(t: Turtle, size: float) -> None:
    """Makes a simple star will eventaly be used to paint the sky with many of them."""
    if size <= 10:
        return
    else:
        for _ in range(5):
            t.forward(size)
            star(t, size / 3)
            t.left(144)


def stars_in_sky() -> None:
    """Combines the stars and backround fucntion so and processes a grid for the stars to lie on."""
    backround()
    t.color('yellow')
    for i in range(10):
        t.penup()
        x = -500 + (i + 1) * 100
        t.goto(x, 0)
        for j in range(4):
            t.penup()
            t.goto(x + j * 50, j * 100)
            t.pendown()
            star(t, 15)


def leg() -> None:
    """This draws one leg of the Turtle and makes it green."""
    t.begin_fill()
    t.color('green')
    t.right(90)
    t.forward(50)
    i: int = 0
    while (i < 36):
        t.forward(2)
        t.left(5)
        i = i + 1
    t.forward(55)
    t.end_fill()


def eye() -> None:
    """This draws two eyes of the Turtle and makes them black."""
    t.begin_fill()
    t.color('black')
    i: int = 0
    while (i < 361):
        t.forward(0.1)
        t.left(1)
        i = i + 1
    t.end_fill()


def mouth() -> None:
    """Draws the Mouth of the Turtle and makes it red."""
    t.color('red')
    i: int = 0
    while (i < 181):
        t.forward(0.5)
        t.left(1)
        i = i + 1


def face() -> None:
    """Combines the eyes and the mouth of the Turtle and postionts the tutrle so they are near eachother."""
    eye()
    t.penup()
    t.right(90)
    t.forward(25)
    t.pendown()
    mouth()
    t.penup()
    t.forward(25)
    t.pendown()
    eye()


def shell() -> None:
    """Draws the shell of the Tutrle and colors it green."""
    t.begin_fill()
    t.color('green')
    i: int = 0
    while i < 89:
        t.right(2)
        t.forward(6)
        i += 1
    t.setheading(90)
    t.left(90)
    t.forward(345)
    t.end_fill()
    

def head(i: int = 0) -> None:
    """Draws the head around the face making it green is within main because this fucntion is recuruve."""
    if i < 120:
        t.forward(2.8)
        t.right(2)
        return head(i + 1)


def floor() -> None:
    """This adds a simple line so it dose not look like the Turtle is floating in the air."""
    t.pencolor('dark green')
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.right(90)
    t.forward(1000)


def main() -> None:
    """Combines all above fucntion moving the tutle into the postion needed to draw the object."""
    t.hideturtle()
    t.speed(0)
    stars_in_sky()
    t.color('yellow')
    star(t, 10)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.left(90)
    shell()
    t.right(180)
    leg()
    t.penup()
    t.goto(140, 0)
    t.right(90)
    t.pendown()
    leg()
    t.penup()
    t.forward(125)
    t.right(90)
    t.left(180)
    t.forward(53)
    t.right(180)
    t.left(50)
    t.pendown()
    t.begin_fill()
    t.color('green')
    head()
    t.end_fill()
    t.penup()
    t.right(85)
    t.forward(100)
    t.right(90)
    t.pendown()
    face()
    floor()
    

if __name__ == "__main__":
    main()
done()