import turtle
import time
import os

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1000,height=1000)
screen.bgcolor("white")
screen.title("Banco CM - (Turtle Graphics)")

#Crear el  
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color("black")


def write_on_screen(text, x, y, size=16, align="center"):
    writer.clear()
    writer.goto(x, y)
    writer.write(text, align=align, font=("Arial", size, "normal"))


def clear_screen_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_welcome_message():
    clear_screen_console()
    print("=========================================")
    print("        ¡Bienvenido a su Banco CM        ")
    print("=========================================")
    time.sleep(2)

    write_on_screen("¡Bienvenido a su Banco CM!", 0, 100, 24)
    write_on_screen("Preparando su sesión, por favor espere...", 0, 50)
    time.sleep(2)

    for i in range(3):
        write_on_screen(f"{'.' * (i + 1)}", 0, 0, 20)
        time.sleep(1)
    write_on_screen("¡Listo! Presione OK en la consola para continuar.", 0, 0, 20)
    print("¡Listo!\n")
    time.sleep(1.5)


def login():
    username_real = "admin"
    password_real = "123"
    attempts = 0

    while attempts < 3:
        clear_screen_console()
        print("--- INICIO DE SESIÓN ---")
        write_on_screen("--- INICIO DE SESIÓN ---", 0, 100, 20)
        write_on_screen(f"Intentos restantes: {3 - attempts}", 0, 60, 14)

        username_input = screen.textinput("Inicio de Sesión", "Ingrese su nombre de usuario:")
        if username_input is None: # User cancelled
            return False

        password_input = screen.textinput("Inicio de Sesión", "Ingrese su contraseña:")
        if password_input is None: # User cancelled
            return False

        if username_input == username_real and password_input == password_real:
            print("\n¡Inicio de sesión exitoso! Accediendo a su cuenta...")
            write_on_screen("¡Inicio de sesión exitoso! Accediendo a su cuenta...", 0, 0, 18)
            time.sleep(2)
            return True
        else:
            attempts += 1
            print(f"\n¡Error! Usuario o contraseña incorrectos. Le quedan {3 - attempts} intentos.")
            write_on_screen(f"¡Error! Usuario o contraseña incorrectos. Le quedan {3 - attempts} intentos.", 0, 0, 16, "center")
            time.sleep(2.5)
            print("-" * 30)

    print("\nDemasiados intentos fallidos. Su sesión ha sido bloqueada temporalmente.")
    print("Por favor, contacte con soporte.")
    print("Número de soporte: (+506) 6121-2866")
    write_on_screen("Demasiados intentos fallidos. Contacte soporte: 6121-2866", 0, -50, 16)
    time.sleep(5) # Give time to read message in turtle window
    return False

def show_main_menu(user_balance):
    clear_screen_console()
    print("\n--- MENÚ PRINCIPAL BANCO CM ---")
    print("1. Realizar una Transferencia")
    print("2. Cambiar Dólares a Colones")
    print("3. Cambiar Colones a Dólares")
    print("4. Retirar Dinero en Efectivo")
    print("5. Consultar Saldo Actual ")
    print("6. Contactar Ayuda / Soporte")
    print("-----------------------------------")
    print("Presione 'X' para Salir del sistema.")
    print("-----------------------------------\n")

    writer.clear()
    writer.goto(0, 150)
    writer.write("--- MENÚ PRINCIPAL BANCO CM ---", align="center", font=("Arial", 18, "bold"))
    
    menu_options = [
        "1. Realizar una Transferencia",
        "2. Cambiar Dólares a Colones",
        "3. Cambiar Colones a Dólares",
        "4. Retirar Dinero en Efectivo",
        f"5. Consultar Saldo Actual: {user_balance:.2f} Colones",
        "6. Contactar Ayuda / Soporte",
        "Presione 'X' para Salir del sistema."
    ]
    
    y_offset = 100
    for option_text in menu_options:
        writer.goto(0, y_offset)
        writer.write(option_text, align="center", font=("Arial", 14, "normal"))
        y_offset -= 30

def make_transfer(user_balance):
    clear_screen_console()
    print("\n--- TRANSFERENCIAS ---")
    write_on_screen("--- TRANSFERENCIAS ---", 0, 100, 20)
    destination_id_real = "mau"

    attempts_transfer = 0
    while attempts_transfer < 3:
        destination_id_input = screen.textinput("Transferencia", "Ingrese el ID de la cuenta destino (o 'B' para volver):").lower()
        if destination_id_input is None or destination_id_input == 'b':
            write_on_screen("Operación de transferencia cancelada.", 0, 0, 16)
            time.sleep(2)
            return user_balance

        if destination_id_input != destination_id_real:
            attempts_transfer += 1
            print(f"ID incorrecto. Le quedan {3 - attempts_transfer} intentos.")
            write_on_screen(f"ID incorrecto. Le quedan {3 - attempts_transfer} intentos.", 0, 0, 16)
            time.sleep(1.5)
            continue

        while True:
            try:
                amount_to_send_input = screen.textinput("Transferencia", "Ingrese el monto que desea transferir (mínimo 1000, o 'B' para volver):")
                if amount_to_send_input is None or amount_to_send_input.lower() == 'b':
                    write_on_screen("Operación de transferencia cancelada.", 0, 0, 16)
                    time.sleep(2)
                    return user_balance

                amount_to_send = float(amount_to_send_input)

                if amount_to_send < 1000:
                    print("¡Advertencia! El monto mínimo para transferencia es 1000.")
                    write_on_screen("¡Advertencia! El monto mínimo para transferencia es 1000.", 0, 0, 16)
                elif amount_to_send > user_balance:
                    print(f"¡Error! No tiene saldo suficiente. Su saldo actual es: {user_balance:.2f} Colones.")
                    write_on_screen(f"¡Error! Saldo insuficiente. Saldo actual: {user_balance:.2f} Colones.", 0, 0, 16)
                else:
                    user_balance -= amount_to_send
                    print(f"\nTransferencia de {amount_to_send:.2f} Colones a {destination_id_input} exitosa.")
                    print(f"Su nuevo saldo es: {user_balance:.2f} Colones.")
                    write_on_screen(f"Transferencia de {amount_to_send:.2f} Colones exitosa.")
                    write_on_screen(f"Nuevo saldo: {user_balance:.2f} Colones.", 0, 16, 16)
                    time.sleep(2.5)
                    return user_balance
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número para el monto.")
                write_on_screen("Entrada inválida. Ingrese un número.", 0, 0, 16)
            time.sleep(1.5)

    if attempts_transfer == 3:
        print("\nDemasiados intentos de ID. Operación de transferencia cancelada.")
        write_on_screen("Demasiados intentos de ID. Transferencia cancelada.", 0, 0, 16)
    time.sleep(2)
    return user_balance

def convert_dollars_to_colones(user_balance):
    clear_screen_console()
    print("\n--- CAMBIO: DÓLARES a COLONES ---")
    write_on_screen("--- CAMBIO: DÓLARES a COLONES ---", 0, 100, 20)

    while True:
        try:
            quantity_dollars_input = screen.textinput("Cambio Dólares a Colones", "Ingrese la cantidad de DÓLARES a cambiar (o 'B' para volver):")
            if quantity_dollars_input is None or quantity_dollars_input.lower() == 'b':
                return user_balance

            quantity_dollars = float(quantity_dollars_input)
            if quantity_dollars <= 0:
                print("La cantidad de dólares debe ser mayor que cero.")
                write_on_screen("La cantidad de dólares debe ser mayor que cero.", 0, 0, 16)
                time.sleep(1.5)
                continue

            dollar_value_input = screen.textinput("Cambio Dólares a Colones", "Ingrese el valor actual del dólar (ej. 520.00, o 'B' para volver):")
            if dollar_value_input is None or dollar_value_input.lower() == 'b':
                return user_balance

            dollar_value = float(dollar_value_input)
            if dollar_value <= 0:
                print("El valor del dólar debe ser mayor que cero.")
                write_on_screen("El valor del dólar debe ser mayor que cero.", 0, 0, 16)
                time.sleep(1.5)
                continue

            colones_obtained = quantity_dollars * dollar_value
            user_balance += colones_obtained
            print(f"\nUsted recibirá: {colones_obtained:.2f} COLONES.")
            print(f"Su nuevo saldo es: {user_balance:.2f} Colones.")
            write_on_screen(f"Recibirá: {colones_obtained:.2f} COLONES. Nuevo saldo: {user_balance:.2f} Colones.", 0, 0, 16)
            print("¡Gracias por confiar en nosotros!")
            time.sleep(3)
            break
        except ValueError:
            print("Error: Por favor, ingrese solo números para las cantidades.")
            write_on_screen("Error: Ingrese solo números.", 0, 0, 16)
            time.sleep(2)
    return user_balance

def convert_colones_to_dollars(user_balance):
    clear_screen_console()
    print("\n--- CAMBIO: COLONES a DÓLARES ---")
    write_on_screen("--- CAMBIO: COLONES a DÓLARES ---", 0, 100, 20)

    while True:
        try:
            quantity_colones_input = screen.textinput("Cambio Colones a Dólares", "Ingrese la cantidad de COLONES a cambiar (o 'B' para volver):")
            if quantity_colones_input is None or quantity_colones_input.lower() == 'b':
                return user_balance

            quantity_colones = float(quantity_colones_input)
            if quantity_colones <= 0:
                print("La cantidad de colones debe ser mayor que cero.")
                write_on_screen("La cantidad de colones debe ser mayor que cero.", 0, 0, 16)
                time.sleep(1.5)
                continue
            if quantity_colones > user_balance:
                print(f"¡Error! No tiene suficientes colones. Su saldo actual es: {user_balance:.2f} Colones.")
                write_on_screen(f"¡Error! Saldo insuficiente. Saldo actual: {user_balance:.2f} Colones.", 0, 0, 16)
                time.sleep(1.5)
                continue

            dollar_value_input = screen.textinput("Cambio Colones a Dólares", "Ingrese el valor actual del dólar (ej. 520.00, o 'B' para volver):")
            if dollar_value_input is None or dollar_value_input.lower() == 'b':
                return user_balance

            dollar_value = float(dollar_value_input)
            if dollar_value <= 0:
                print("El valor del dólar no puede ser cero o negativo.")
                write_on_screen("El valor del dólar no puede ser cero o negativo.", 0, 0, 16)
                time.sleep(1.5)
                continue

            dollars_obtained = quantity_colones / dollar_value
            user_balance -= quantity_colones
            print(f"\nUsted recibirá: {dollars_obtained:.2f} DÓLARES.")
            print(f"Su nuevo saldo es: {user_balance:.2f} Colones.")
            write_on_screen(f"Recibirá: {dollars_obtained:.2f} DÓLARES. Nuevo saldo: {user_balance:.2f} Colones.", 0, 0, 16)
            time.sleep(3)
            break
        except ValueError:
            print("Error: Por favor, ingrese solo números para las cantidades.")
            write_on_screen("Error: Ingrese solo números.", 0, 0, 16)
            time.sleep(2)
    return user_balance

def withdraw_money(user_balance):
    clear_screen_console()
    print("\n--- RETIRO DE DINERO ---")
    print(f"Su saldo disponible es: {user_balance:.2f} Colones.")
    write_on_screen("--- RETIRO DE DINERO ---", 0, 100, 20)
    write_on_screen(f"Su saldo disponible es: {user_balance:.2f} Colones.", 0, 60, 16)

    while True:
        try:
            amount_to_withdraw_input = screen.textinput("Retiro de Dinero", "Digite la cantidad de dinero que desea retirar (o 'B' para volver):")
            if amount_to_withdraw_input is None or amount_to_withdraw_input.lower() == 'b':
                return user_balance

            amount_to_withdraw = float(amount_to_withdraw_input)

            if amount_to_withdraw <= 0:
                print("El monto a retirar debe ser mayor que cero.")
                write_on_screen("El monto a retirar debe ser mayor que cero.", 0, 0, 16)
            elif amount_to_withdraw > user_balance:
                print("¡Lo sentimos! Saldo insuficiente para realizar este retiro.")
                write_on_screen("¡Lo sentimos! Saldo insuficiente.", 0, 0, 16)
            else:
                print("\nProcesando su solicitud de retiro...")
                write_on_screen("Procesando su solicitud de retiro...", 0, 0, 16)
                time.sleep(2)
                user_balance -= amount_to_withdraw
                print(f"Cantidad Retirada: {amount_to_withdraw:.2f} Colones")
                print(f"Saldo Restante: {user_balance:.2f} Colones")
                print("\n¡Transacción finalizada con éxito!")
                write_on_screen(f"Retirada: {amount_to_withdraw:.2f} Colones. Saldo restante: {user_balance:.2f} Colones.", 0, 0, 16)
                time.sleep(3)
                break
        except ValueError:
            print("Error: Por favor, ingrese un número válido para el monto.")
            write_on_screen("Error: Ingrese un número válido.", 0, 0, 16)
        time.sleep(2)
    return user_balance

def check_balance(user_balance):
    clear_screen_console()
    print("\n--- CONSULTA DE SALDO ---")
    print("Consultando su saldo, por favor espere...")
    write_on_screen("--- CONSULTA DE SALDO ---", 0, 100, 20)
    write_on_screen("Consultando su saldo, por favor espere...", 0, 50, 16)
    time.sleep(2)
    print(f"\nSu saldo actual es: {user_balance:.2f} Colones.")
    write_on_screen(f"Su saldo actual es: {user_balance:.2f} Colones.", 0, 0, 18)
    time.sleep(3)
    return user_balance

def contact_help():
    clear_screen_console()
    print("\n--- AYUDA Y SOPORTE ---")
    print("Si tiene algún problema o consulta, no dude en contactarnos.")
    time.sleep(1.5)
    print("\nNúmero de Teléfono de Soporte:")
    print("         6121-2866           ")
    print("\n¡Gracias por preferir Banco CM!")
    write_on_screen("--- AYUDA Y SOPORTE ---", 0, 100, 20)
    write_on_screen("Si tiene algún problema, no dude en contactarnos.", 0, 50, 16)
    write_on_screen("Número de Teléfono de Soporte: 6121-2866", 0, 0, 18)
    write_on_screen("¡Gracias por preferir Banco CM!", 0, -50, 16)
    time.sleep(3)

def main():
    user_balance = 45897.00
    show_welcome_message()

    if login():
        while True:
            show_main_menu(user_balance)
            # Use textinput for menu option to show it in turtle window
            option = screen.textinput("Menú Principal", "Por favor, elija una opción (o 'X' para Salir):").strip().lower()

            if option is None or option == 'x':
                clear_screen_console()
                print("\nGracias por usar Banco CM. ¡Hasta luego!")
                write_on_screen("Gracias por usar Banco CM. ¡Hasta luego!", 0, 0, 20)
                time.sleep(2)
                break

            try:
                option = int(option)

                if option == 1:
                    user_balance = make_transfer(user_balance)
                elif option == 2:
                    user_balance = convert_dollars_to_colones(user_balance)
                elif option == 3:
                    user_balance = convert_colones_to_dollars(user_balance)
                elif option == 4:
                    user_balance = withdraw_money(user_balance)
                elif option == 5:
                    user_balance = check_balance(user_balance)
                elif option == 6:
                    contact_help()
                else:
                    print("\nOpción inválida. Por favor, elija un número del 1 al 6, o 'X' para salir.")
                    write_on_screen("Opción inválida. Elija un número del 1 al 6 o 'X'.", 0, 0, 16)
                    time.sleep(2)
            except ValueError:
                print("\nEntrada inválida. Por favor, ingrese un número para la opción o 'X' para salir.")
                write_on_screen("Entrada inválida. Ingrese un número o 'X'.", 0, 0, 16)
                time.sleep(2)
            print("\n" + "="*50 + "\n")
            time.sleep(1)
    
    # Close the turtle window when the main loop finishes
    turtle.bye()


if __name__ == "__main__":
    main()