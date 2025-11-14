import random 
def menu():
    while True:
        print('===MENU PRINCIPAL===')
        print("1. Primer Premio")
        print("2. Segundo Premio")
        print("3. Tercer Premio")
        print("4. Reventado ")
        print("5. Salir")
        print("")
        print("")
        opcion = input("Elije una opcion: ")
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            reventado()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opcion no valida, intenta de nuevo")
menu()
def opcion1():#bhjm.bki
    def numero1():
        n1= random.randrange(0,99)
        print("El número es....", n1);
    def serie1():
        s1= random.randint(100,999)
        print("Su serie es de....", s1)
    def regresar():
        print("")
        print("Regresando...")
        print("")
    def mdn():
        while True:
            print("====Opciones====")
            print("")
            print("1. Número")
            print("2. Serie ")
            print("3. Regresar al menu")
            print("")
            opcion = input("Elije una opcion: ")
            if opcion == "1":
                numero1()
            elif opcion == "2":
                serie1()
            elif opcion == "3":
                regresar()
                break
            else:
                print("Opcion no valida, intenta de nuevo")
    mdn()

def opcion2():
    def numero2():
        n1= random.randrange(0,99)
        print("El número es....", n1);
    def serie2():
        s1= random.randint(100,999)
        print("Su serie es de....", s1)
    def regresar():
        print("")
        print("Regresando...")
        print("")
    def mdn():
        while True:
            print("====Opciones====")
            print("")
            print("1. Número")
            print("2. Serie ")
            print("3. Regresar al menu")
            print("")
            opcion = input("Elije una opcion: ")
            if opcion == "1":
                numero2()
            elif opcion == "2":
                serie2()
            elif opcion == "3":
                regresar()
                break
            else:
                print("Opcion no valida, intenta de nuevo")
    mdn()
def opcion3():
    def numero3():
        n1= random.randrange(0,99)
        print("El número es....", n1);
    def serie3():
        s1= random.randint(100,999)
        print("Su serie es de....", s1)
    def regresar():
        print("")
        print("Regresando...")
        print("")
    def mdn():
        while True:
            print("====Opciones====")
            print("")
            print("1. Número")
            print("2. Serie ")
            print("3. Regresar al menu")
            print("")
            opcion = input("Elije una opcion: ")
            if opcion == "1":
                numero3()
            elif opcion == "2":
                serie3()
            elif opcion == "3":
                regresar()
                break
            else:
                print("Opcion no valida, intenta de nuevo")
    mdn()
def reventado():
    print("")
    re= random.randrange(1,4)
    
    if re == 1:
        print("Es Bola Roja")
        print("")
    if re == 2:
        print("Es Bola Blanca")
        print("")
    if re == 3:
        print("Es Bola Reventada")
        print("")
def salir():
    print("4")
    print("Hasta luego, Suerte la Proxima vez")3