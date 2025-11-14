from turtle import *
from math import *

# Configuración inicial
speed(0)
bgcolor("black")
goto(0, -40)

# Dibujar pétalos (hojas)
for i in range(16):
    for j in range(18):
        color("#FFA216") # Color naranja/amarillo para los pétalos
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)


color('black')
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')  
golden_ang = 137.508
phi = golden_ang * (pi / 180)

for i in range(140):
    r = 4 * sqrt(i)
    theta = i * phi
    x = r * cos(theta)
    y = r * sin(theta)
    penup()
    goto(x, y)
    setheading(i * golden_ang)
    pendown()
    stamp()




penup() 
y_offset = -30
goto(0, y_offset) 
pendown()

color("white") 
write("F", align="center", font=("Arial", 30, "bold")) 

hideturtle() 
done()