# --- CONFIGURACIÓN GLOBAL ---
TASA_CAMBIO_DOLAR = 580.00
SALDO_INICIAL = 45897.00 # Saldo en Colones (₡)

class CajeroAutomatico:
    def __init__(self, saldo_inicial, tasa_dolar):
        # El estado de la cuenta se mantiene dentro del objeto
        self.saldo_actual = saldo_inicial
        self.tasa_cambio_dolar = tasa_dolar
        self.ejecutandose = True

    def _obtener_entrada_numerica(self, mensaje):
        """Manejador para obtener una entrada numérica válida desde la consola."""
        while True:
            try:
                entrada = input(mensaje).strip().lower()
                if entrada in ('b', 'x'):
                    return None
                
                valor = float(entrada)
                # Solo se asegura que sea un monto positivo.
                if valor <= 0:
                    print("\n[Advertencia] El monto debe ser positivo. Intente de nuevo o 'B' para volver.")
                    continue
                return valor
            except ValueError:
                print("\n[Error] Entrada inválida. Por favor, ingrese solo números, 'B' para volver, o 'X' para salir.")

    def _mostrar_menu(self):
        """Muestra las opciones del menú principal."""
        print("\n" + "="*35)
        print(" 🏦 --- MENÚ BANCO COLOM ---")
        print("="*35)
        print("1. Transferir ")
        print("2. Cambiar Dólares a Colones ")
        print("3. Cambiar Colones a Dólares ")
        print("4. Retirar Efectivo ")
        print("5. **CONSULTAR SALDO**")
        print("6. Ingresar saldo")
        print("7. Salir (X)")
        print("-" * 35)

    # --- 1. Transferir ---
    def realizar_transferencia(self):
        print("\n--- TRANSFERENCIA ---")
        
        destino_input = input("Ingrese el ID de la cuenta destino ('B' para volver): ").strip().lower()
        if destino_input == 'b':
            print("Transferencia cancelada.")
            return
        
        monto_a_enviar = self._obtener_entrada_numerica(
            f"Saldo: ₡{self.saldo_actual:,.2f}. Ingrese el monto a enviar: "
        )

        if monto_a_enviar is None:
            print("Transferencia cancelada.")
            return

        if monto_a_enviar > self.saldo_actual:
            print(f"\n❌ ¡Error! Saldo insuficiente. Tiene: ₡{self.saldo_actual:,.2f}.")
        else:
            self.saldo_actual -= monto_a_enviar
            print(f"\n✅ ¡EXITOSO! Transferencia de ₡{monto_a_enviar:,.2f} a la cuenta {destino_input}.")
            self.consultar_saldo(mensaje_adicional="Nuevo saldo: ")

    # --- 2. Dólares a Colones ---
    def cambiar_dolares_a_colones(self):
        print("\n--- CAMBIO: USD -> ₡ ---")
        print(f"Tasa de compra: 1 USD = ₡{self.tasa_cambio_dolar:,.2f}.")

        cantidad_dolares = self._obtener_entrada_numerica(
            "Ingrese la cantidad de DÓLARES a cambiar ('B' para volver): "
        )
        if cantidad_dolares is None:
            return
        
        colones_obtenidos = cantidad_dolares * self.tasa_cambio_dolar
        self.saldo_actual += colones_obtenidos

        print(f"\nRecibe: ₡{colones_obtenidos:,.2f} COLONES.")
        self.consultar_saldo(mensaje_adicional="Nuevo saldo: ")

    # --- 3. Colones a Dólares ---
    def cambiar_colones_a_dolares(self):
        print("\n--- CAMBIO: ₡ -> USD ---")
        print(f"Tasa de venta: 1 USD = ₡{self.tasa_cambio_dolar:,.2f}.")

        cantidad_colones = self._obtener_entrada_numerica(
            f"Saldo: ₡{self.saldo_actual:,.2f}. Ingrese COLONES a cambiar ('B' para volver): "
        )
        if cantidad_colones is None:
            return

        if cantidad_colones > self.saldo_actual:
            print(f"\n❌ ¡Error! Saldo insuficiente. Saldo actual: ₡{self.saldo_actual:,.2f}.")
            return

        dolares_obtenidos = cantidad_colones / self.tasa_cambio_dolar
        self.saldo_actual -= cantidad_colones

        print(f"\nRecibe: ${dolares_obtenidos:,.2f} DÓLARES.")
        self.consultar_saldo(mensaje_adicional="Nuevo saldo: ")

    # --- 4. Retirar Efectivo ---
    def retirar_dinero(self):
        print("\n--- RETIRO DE EFECTIVO ---")

        monto_a_retirar = self._obtener_entrada_numerica(
            f"Saldo: ₡{self.saldo_actual:,.2f}. Cantidad a retirar ('B' para volver): "
        )
        if monto_a_retirar is None:
            return

        if monto_a_retirar > self.saldo_actual:
            print("\n❌ ¡Error! Saldo insuficiente.")
        else:
            self.saldo_actual -= monto_a_retirar
            print(f"\n✅ ¡RETIRO EXITOSO! Retirado: ₡{monto_a_retirar:,.2f}.")
            self.consultar_saldo(mensaje_adicional="Saldo restante: ")

    # --- 5. Consultar Saldo ---
    def consultar_saldo(self, mensaje_adicional=""):
        """Muestra el saldo actual de la cuenta."""
        print(f"\n--- SALDO ACTUAL ---")
        print(f"\n*********************************************")
        print(f"* {mensaje_adicional} SU SALDO ES: ₡{self.saldo_actual:,.2f} *")
        print(f"*********************************************")

    # ---6. Ingresar saldo ---
    def ingresar_saldo(self):
        valor_ingresado = input("Ingrese el valor deceado: ")
        self.saldo_actual + valor_ingresado
        print(f"*  SU SALDO ES: ₡{self.saldo_actual:,.2f} *")


    # --- Bucle Principal ---
    def bucle_principal(self):
        """El bucle principal para la interacción del menú."""
        opciones_map = {
            '1': self.realizar_transferencia,
            '2': self.cambiar_dolares_a_colones,
            '3': self.cambiar_colones_a_dolares,
            '4': self.retirar_dinero,
            '5': self.consultar_saldo,
            "6": self.ingresar_saldo,
        }
        
        while self.ejecutandose:
            self._mostrar_menu()
            opcion = input("Elija una opción : ").strip().lower()

            if opcion in ('x', 'c'):
                self.ejecutandose = False
                break
            accion = opciones_map.get(opcion)
            if accion:
                accion()
            else:
                print("\n[Advertencia] Opción no reconocida. Intente de nuevo.")
def autenticar_usuario():
    """Maneja el inicio de sesión con 3 intentos máximos."""
    USUARIO_CORRECTO = "admin"
    CONTRASENA_CORRECTA = "123"
    MAX_INTENTOS = 3
    for intento in range(1, MAX_INTENTOS + 1):
        print("\n--- INICIO DE SESIÓN ---")
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        
        if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
            print("\n¡Acceso concedido! Bienvenido, Usuario.")
            return True
        else:
            intentos_restantes = MAX_INTENTOS - intento
            if intentos_restantes > 0:
                print(f"❌ Error. Intento {intento}/{MAX_INTENTOS}. Le quedan {intentos_restantes} intentos.")
            else:
                print("❌ Ha superado el número máximo de intentos. Cerrando el programa.")
                return False
    return False
def main():
    """Punto de entrada de la aplicación."""
    
    if autenticar_usuario():
        cajero = CajeroAutomatico(SALDO_INICIAL, TASA_CAMBIO_DOLAR)
        cajero.bucle_principal()
        print("\nGracias por usar el Banco Colom. ¡Hasta luego! 👋")
    else:
        pass
if __name__ == "__main__":
    main()