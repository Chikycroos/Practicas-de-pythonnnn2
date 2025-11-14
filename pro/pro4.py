import turtle

def draw_heart():
    """
    Dibuja un corazón usando la tortuga.
    """
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
    turtle.forward(113)
    turtle.end_fill()

def love_message_in_heart():
 

    screen = turtle.Screen()
    screen.setup(width=600, height=500)
    screen.bgcolor("black")
    screen.tracer(0) 


    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, -150) 

    # Dibujar el corazón
    pen.pendown()
    draw_heart()
    pen.penup()

    
    pen.goto(0, 0) 
    pen.color("white")
    pen.write("¡Sea sapo!", align="center", font=("Arial", 24, "bold"))

    screen.update() 
    turtle.done() 

if __name__ == "__main__":
    love_message_in_heart()