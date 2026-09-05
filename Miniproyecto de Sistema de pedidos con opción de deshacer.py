#=============================================
# SISTEMA DE PEDIDOS CON OPCIÓN DE DESHACER
#==============================================


#==============================================
# Clase donde guardo la información del pedido
#==============================================
class Pedido:
    def __init__(self, producto, cantidad, precio):
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio

#===============================================
# Método mostrar
# Aqui se muestra la información del pedido
#===============================================
    def mostrar(self):
        print(f"Producto: {self.producto} | Cantidad: {self.cantidad} | Precio: C$ {self.precio:.2f}")

#===============================================
# Clase donde se maneja la pila de pedidos
#===============================================
class PilaPedidos:
    def __init__(self):
        self.pila = []

#=======================================
# Método agregar
# agregamos el pedido a la Pila (append)
#=======================================
    def agregar(self, pedido):
        self.pila.append(pedido)

#================================================
# Método deshacer
# Aqui se quita el último pedido agregado (pop)
#================================================
    def deshacer(self):
        if len(self.pila) > 0:
            return self.pila.pop()
        else:
            return None

#================================================
# Método mostrar de pilapedidos
# Se muestran los pedidos que están en la pila
#================================================
    def mostrar(self):
        if len(self.pila) == 0:
            print("No hay pedidos registrados.")
        else:
            print("\n--- LISTA DE PEDIDOS ---")
            for pedido in self.pila:
                pedido.mostrar()

#=========================================
# Método para calcular el total
#=========================================
    def total(self):
        if len(self.pila) == 0:
            print("No hay pedidos registrados para calcular el total.")
            return

        total = 0
        for pedido in self.pila:
            total += pedido.cantidad * pedido.precio

        print(f"Total de todos los pedidos: C$ {total:.2f}")

#================================================
# Función Menú
# Esta es la parte principal del programa (controla las opciones del programa)
#================================================
def menu():
    pila_pedidos = PilaPedidos()

#================================================
# El Menú se va a mantener hasta que decida salir
#================================================
    while True:
        print("\n===== SISTEMA DE PEDIDOS =====")
        print("1. Agregar pedido")
        print("2. Mostrar pedidos")
        print("3. Deshacer último pedido")
        print("4. Ver total")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

#================================================
# Opción para registrar nuevo pedido con validación
#================================================
        if opcion == "1":
            # Validar nombre del producto (que no sea un texto vacío ni solo números)
            while True:
                producto = input("Ingrese el producto: ").strip()
                if not producto:
                    print(" Error: El nombre del producto no puede estar vacío.")
                elif not any(char.isalpha() for char in producto):
                    print(" Error: El nombre del producto debe contener letras (no puede ser solo números ni símbolos).")
                else:
                    break

            # Validar cantidad (debe ser entero y mayor a 0)
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad: "))
                    if cantidad > 0:
                        break
                    else:
                        print(" Error: La cantidad debe ser un número entero mayor a 0.")
                except ValueError:
                    print(" Error: Debe ingresar un número entero válido (sin letras ni decimales).")

            # Validar precio (debe ser un número positivo)
            while True:
                try:
                    precio = float(input("Ingrese el precio (C$): "))
                    if precio > 0:
                        break
                    else:
                        print(" Error: El precio debe ser un valor mayor a 0.")
                except ValueError:
                    print(" Error: Debe ingresar un número decimal válido (ejemplo: 25.50).")

            # Crear y agregar el pedido tras pasar las validaciones
            pedido = Pedido(producto, cantidad, precio)
            pila_pedidos.agregar(pedido)

            print(" Pedido agregado correctamente.")

#================================================
# Opción para ver los pedidos registrados
#================================================
        elif opcion == "2":
            pila_pedidos.mostrar()

#================================================
# Opción para quitar el último pedido
#================================================
        elif opcion == "3":
            pedido = pila_pedidos.deshacer()

            if pedido is not None:
                print(f" Pedido deshecho: {pedido.producto}")
            else:
                print(" No hay pedidos para deshacer.")

#=========================================
# Opción para ver el total
#=========================================
        elif opcion == "4":
            pila_pedidos.total()

#================================================
# Opción para terminar el programa
#================================================
        elif opcion == "5":
            print("Pedido Terminado.")
            print("¡¡Gracias por usar el sistema!! ☺️") 
            break

        else:
            print(" Opción no válida. Intente de nuevo con un número del 1 al 5.")

#================================================
# Aqui ya puedo iniciar el programa
#================================================
menu()