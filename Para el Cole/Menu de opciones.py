#import os
def saludar():
    print("\U0001F44B","Hola, bienvenido al prgrama.")
    # os.system("start cmd /max /k python Hola_mundo.py")
def sumar():
    a= int(input("Ingresa el primer numero: "))
    b= int(input("Ingresa el segundo numero: "))
    print(f"La suma es: {a + b}")

def despedir():
    print("\U0001F44B","Gracias por usar el programa. ¡Hasta luego!")

def menu():
    while True:
        print('\n===MENU PRINCIPAL===')
        print("1. Saludar")
        print("2. Sumar dos numeros")
        print("3. Despedirse y salir")
        print('======================')

        opcion = input("Elije una opcion: ")
        if opcion == "1":
            saludar()
        elif opcion == "2":
            sumar()
        elif opcion == "3":
            despedir()
            break
        else:
            print("⚠️Opcion no valida, intenta de nuevo")
#Ejecutar el menu
menu()

