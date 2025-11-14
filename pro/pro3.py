import turtle
import math
import time

def pulsating_love_message():
   
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("black")
    screen.tracer(0) # Desactivar la actualización automática para animación suave

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("red")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 0) # Centrar el texto

    # Bucle principal de la animación
    start_time = time.time()
    while True:
        # Calcular un valor de pulsación usando seno para un efecto suave
        # El valor oscilará entre -1 y 1. Lo ajustamos para que sea entre 0.5 y 1.5
        pulsation_factor = 1 + 0.5 * math.sin((time.time() - start_time) * 3) # Multiplicamos por 3 para una pulsación más rápida

        # Calcular el tamaño de la fuente basado en el factor de pulsación
        font_size = int(50 * pulsation_factor)
        if font_size < 30: # Asegurarse de que el tamaño mínimo no sea demasiado pequeño
            font_size = 30
        elif font_size > 70: # Asegurarse de que el tamaño máximo no sea demasiado grande
            font_size = 70

        pen.clear() # Borrar el texto anterior
        pen.write("me la chupas?", align="center", font=("Arial", font_size, "bold"))
        screen.update() # Actualizar la pantalla

        time.sleep(0.05) # Pequeña pausa para controlar la velocidad de la animación

# Ejecutar la función
if __name__ == "__main__": # ¡Esta es la línea corregida!
    pulsating_love_message()