"""Making a bumble bee."""

__author__ = "730313338"

from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None: 
    """Construct turtle objects."""
    bee: Turtle = Turtle()
    orient: bool = True
    draw_square(bee, 100, 100, 90)
    draw_triangles(bee, 100, 100, orient)
    draw_triangles(bee, 100, 10, not orient)
    draw_circle(bee, 75, 30, 30)
    draw_triangle(bee, 190, 80,)
    draw_bees()
    done()


def draw_square(body: Turtle, x: float, y: float, width: float) -> None:
    """Draw a yellow body."""
    body.penup()
    body.goto(x, y)
    body.setheading(0.0)
    body.pendown()
    body.color("yellow")
    body.begin_fill()
    i: int = 0
    while i < 4: 
        body.forward(width)
        body.right(90)
        i = i + 1
    body.end_fill()    
          

def draw_triangles(wings: Turtle, x: float, y: float, orient: bool) -> None:
    """Draw black wings."""
    angle: int
    if orient: 
        angle = 120
    else:
        angle = 240   
    wings.color("black")
    wings.penup()
    wings.goto(x, y)
    wings.setheading(0.0)
    wings.pendown()
    i: int = 0
    while i < 3: 
        wings.forward(50)
        wings.left(angle)
        i = i + 1


def draw_circle(head: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a head with a yellow pen."""
    head.penup()
    head.goto(x, y)
    head.setheading(0.0)
    head.pendown()
    head.color("yellow")
    head.circle(30)


def draw_triangle(stinger: Turtle, x: float, y: float) -> None: 
    """Draw a black stinger."""
    stinger.penup()
    stinger.goto(x, y)
    stinger.setheading(0.0)
    stinger.pendown()
    stinger.color("black")
    stinger.begin_fill()
    stinger.right(45)
    stinger.forward(20)
    stinger.right(90)
    stinger.forward(20)    
    stinger.end_fill()    


def draw_bees() -> None:
    """Draw max 6 bees on random places on scene."""
    bee: Turtle = Turtle()
    orient: bool = True
    i: int = 0 
    max: int = 5
    while i < max:
        x: int = randint(-200, 200)
        y: int = randint(-200, 200) 
        draw_square(bee, x, y, 90)
        draw_triangles(bee, x, y, orient)
        draw_triangles(bee, x, y - 90, not orient)
        draw_circle(bee, x - 25, y - 70, 30)
        draw_triangle(bee, x + 90, y - 20,)
        i += 1


if __name__ == "__main__":
    main()