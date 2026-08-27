"""
Un profesor necesita administrar las calificaciones de sus estudiantes,
calcular promedios, determinar quienes aprueban o reprueban, y generar
un reporte final ordenado por rendimiento.

CONCEPTOS DE PROGRAMACION QUE DEBERAN APLICAR:
- Variables y tipos de datos (str, int, float, bool, list, dict)
- Entrada/salida de datos (input, print)
- Operadores aritméticos, relacionales y logicos
- Estructuras condicionales (if, elif, else)
- Estructuras repetitivas (for, while)
- Funciones (con y sin parametros, con y sin retorno)
- Listas y diccionarios
- Clases y objetos (POO)
- Encapsulamiento, herencia, polimorfismo
- Manejo de excepciones (try, except)
- Módulos y funciones principales (__main__)
========================================================================
"""
# ========================================================================
# 1. CONSTANTES GLOBALES
# ========================================================================
NOTA_MINIMA_APROBACION = 3.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA = 0.0
CANTIDAD_NOTAS = 5

# ========================================================================
# 2. FUNCIONES AUXILIARES (sin retorno, sin parametros)
# ========================================================================
def funcion_mostrar_linea():
    """Imprime una linea de separacion, funcion sin parametros y sin retorno"""
    print("-" * 80)

def funcion_mostrar_encabezado(titulo):
    """Imprime un encabezado, funcion con parametros y sin retorno"""
    funcion_mostrar_linea()
    print(f"{titulo}")
    funcion_mostrar_linea()

def funcion_pausar():
    """Pausa la ejecucion del programa hasta que el usuario presione una tecla, funcion sin parametros"""
    input("Presione una tecla para continuar: ")

# ========================================================================
# 3. FUNCIONES CON RETORNO (operaciones y validaciones)
# ========================================================================
def funcion_leer_texto(mensaje):
    """Lee un texto desde la entrada estandar, funcion con parametros y con retorno"""
    while True:
        texto = input(f"{mensaje}").strip()
        if texto:
            return texto
        print("Advertencia: El texto no puede estar vacio. Intente nuevamente.")

def funcion_leer_numero(mensaje, minimo, maximo):
    """Lee un numero flotante y valida un rango"""
    while True:
        try:
            numero = float(input(f"{mensaje}"))
            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"Advertencia: El numero debe estar entre {minimo} y {maximo}. Intente nuevamente.")
        except ValueError:
            print("Error: Entrada invalida. Por favor ingrese un numero valido.")

        def funcion_calcular_promedio(notas):
            if(len(notas) == 0):
                return 0.0

        return sum(notas) / len(notas)

def funcion_determinar_estado(promedio):
    """Determina el estado del estudiante segun su promedio"""
    if promedio >= NOTA_MINIMA_APROBACION:
       return "Aprobado"
    else:
         return "Reprobado"

def funcion_determinar_estado(promedio):
    """Determina el estado del estudiante según su promedio"""
    if promedio >= NOTA_MINIMA_APROBACION:
        return "Aprobado"
    else:
        return "Reprobado"

def funcion_determinar_mencion(promedio):
    """Determina la mención del estudiante según su promedio"""
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy Bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Regular"
    else:
        return "En recuperacion"

def funcion_determinar_rendimiento(promedio):
    """Determina el rendimiento del estudiante según su promedio"""
    #Operadores logicos: and, or, not
    if promedio >= 4.7 and promedio <= NOTA_MAXIMA:
        return "ALTO"
    elif promedio >= 4.0 and promedio < 4.7:
        return "MEDIO"
    elif promedio >= NOTA_MINIMA_APROBACION and promedio < 4.0:
        return "BAJO"
    else:
        return "MUY BAJO"

    
#========================================================================
#4 CLASE ESTUDIANTE (POO - encapsulamiento, herencia, polimorfismo)
#========================================================================

class Estudiante:
    """
    Clase que representa a un estudiante con sus atributos y métodos.
    Encapsulamiento: Los atributos son privados y se accede a ellos mediante métodos.
    """

   #Variable de clase
    _cantidad_estudiantes = 0

    def __init__(self, NombreCompleto, edad, grado):
        """
        Inicializa un objeto Estudiante con nombre, apellido y lista de notas.
        Contructor de la clase
        self hace referncia al objeto actual
        """
        Estudiante._cantidad_estudiantes += 1
        self._id = Estudiante._cantidad_estudiantes
        self._NombreCompleto = NombreCompleto
        self._edad = edad
        self._grado = grado
        self._notas = [] #Declaracion de lista vacia que recibe las notas
        self._promedio = 0.0
        self._estado = ""
        self._mencion = ""
        self._rendimiento = ""

#======== GETTERS (Encapsulamiento) ========
@property
def id(self):
    """Devuelve el ID del estudiante"""
    return self._id

@property
def nombreCompleto(self):
    """Devuelve el nombre completo del estudiante"""
    return self._nombreCompleto

@property
def edad(self):
    """Devuelve la edad del estudiante"""
    return self._edad

@property
def grado(self):
    """Devuelve el grado del estudiante"""
    return self._grado

@property
def notas(self):
    """Devuelve el grado del estudiante"""
    return self._notas.copy()

@property
def promedio(self):
    """Devuelve el promedio del estudiante"""
    return self._promedio

@property
def estado(self):
    """Devuelve el estado del estudiante"""
    return self._estado

@property
def mencion(self):
    """Devuelve la mencion del estudiante"""
    return self._mencion

@property
def rendimiento(self):
    """Devuelve el rendimiento del estudiante"""
    return self._rendimiento

#======== SETTERS (modificadores) ========
@edad.setter
def edad(self, valor):
    """Establece la edad del estudiante"""
    if 0 < valor < 65:
        self._edad = valor
    else:
        raise ValueError("La edad debe ser un numero positivo.")

# ======= MÉTODOS DE INSTANCIA =======

    def funcion_agregar_nota(self, nota):
        """Agrega una nota a la lista de estudiantes"""
        if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            self._notas.append(nota)
        else:
            raise ValueError(f"La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}.")

    def funcion_calcular_resultados(self):
        """Calcula el promedio, estado, mencion y rendimiento del estudiante"""
        self._promedio = self._funcion_calcular_promedio()
        self._estado = funcion_determinar_estado(self._promedio)
        self._mencion = funcion_determinar_mencion(self._promedio)
        self._rendimiento = funcion_determinar_rendimiento(self._promedio) 

    def funcion_esta_aprobado(self):
        """Devuelve True si el estudiante esta aprobado, False en caso contrario"""
    return self._estado == "APROBADO"

    # ------- MÉTODOS ESPECIALES -------

    def __str__(self):
        """Devuelve una representación en cadena del estudiante"""
        icono_estado = "✅" if self.funcion_esta_aprobado() == "APROBADO" else "❌"
        return (f"ID: {self._id}, Nombre: {self._nombreCompleto}, Edad: {self._edad}, "
                f"Grado: {self._grado}, Promedio: {self._promedio:.2f}, "
                f"Estado: {self._estado}, Mención: {self._mencion}, "
                f"Rendimiento: {self._rendimiento}")

    def __lt__(self, other):
        """Compara estudiantes por promedio (menor que -- less than)"""
        if not isinstance(other, Estudiante):
            return NotImplemented
    
        return self._promedio > other._promedio #Mayor promedio significa mejor rendimiento, por lo que se invierte la comparación para ordenar de mayor a menor

#======================================================
# 5 HERENCIA: EstudianteBecado hereda de Estudiante
#======================================================

class EstudianteBecado(Estudiante):
    """
    Clase hija que hereda de Estudiante.
    Representa a un estudiante con beca academica.
    """
    
    def __init__(self, NombreCompleto, edad, grado, porcentaje_beca):
        #Invocar al constructor de la clase padre
        super().__init__(NombreCompleto, edad, grado)
        self._porcentaje_beca = porcentaje_beca
        self._tipo_beca = self._funcion_determinar_tipo_beca()

    def _funcion_determinar_tipo_beca(self):
        """Metodo privado que determina el tipo de beca según el porcentaje"""
        if self._porcentaje_beca >= 80:
            return "Beca Completa C$ 3,000.00"
        elif self._porcentaje_beca >= 60:
            return "Beca Parcial del 60% C$ 1,800.00"
        else:
            return "Beca Minima C$ 1,000.00"

@property
def _porcentaje_beca(self):
    """Devuelve el porcentaje de la beca del estudiante"""
    return self._porcentaje_beca

@property
def _tipo_beca(self):
    """Devuelve el tipo de beca del estudiante"""
    return self._tipo_beca

#Sobrescritura de metodo (Polimorfismo) para calcular resultados con bonus de beca
def funcion_calcular_resultados(self):
    """Calcula los resultados del estudiante becado y aplica un bonus de 0.20 puntos al promedio """
    return super().funcion_calcular_resultados()
    #Los estudiante tienen un bonus de 0.20 puntos en su promedio
    #para efecto de mencion (no afecta al promedio real)
    if self.funcion_esta_aprobado():
        self._promedio += 0.20
        if self._promedio > NOTA_MAXIMA:
            self._promedio = NOTA_MAXIMA

#======================================================
# 6 FUNCIONES DEL MENU PRINCIPAL
#======================================================

def funcion_mostrar_menu():
    """Muestra el menu principal y devuelve la opcion seleccionada"""
    funcion_mostrar_encabezado("SISTEMA DE GESTION DE NOTAS ESCOLARES")
    print("[1] Registrar estudiante regular")
    print("[2] Registrar estudiante becado")
    print("[3] Ver lista de estudiantes")
    print("[4] Ver reporte completo")
    print("[5] Estadisticas del curso")
    print("[6] Buscar estudiante por nombre")
    print("[7] Cargar datos de ejemplo")
    print("[0] Salir")
    funcion_mostrar_linea()

    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if 0 <= opcion <= 7:
                return opcion

            print("Advertencia: Opcion invalida. Intente nuevamente.")
        except ValueError:
            print("Error: Entrada invalida. Por favor ingrese un numero valido.")

def funcion_registrar_estudiante(estudiantes):
    """Registra un estudiante regular"""
    funcion_mostrar_encabezado("REGISTRAR ESTUDIANTE REGULAR")    

    nombre = funcion_leer_texto("Ingrese el nombre completo del estudiante: ")
    edad = funcion_leer_numero("Ingrese la edad del estudiante (18-65): ", 18, 65)
    grado = int(funcion_leer_texto("Ingrese el grado del estudiante: "))

    estudiante = Estudiante(nombre, edad, grado)

    #Ciclo for: Solicitar las 3 notas
    for i in range(CANTIDAD_NOTAS):
        nota = funcion_leer_numero(f"Ingrese la nota {i + 1} (2.0 - 5.0): ", NOTA_MINIMA, NOTA_MAXIMA)
        estudiante.funcion_agregar_nota(nota)

    estudiante.funcion_calcular_resultados()
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado exitosamente.")

#======================================================
# 7. FUNCION PRINCIPAL
#======================================================

def main():
    """FIUNCION PRINCIPAL

    Inicializamos el sistema, crear la lista de estudiantes y gestion
    el bucle principal con un menu interactivo
    """

    #Lista que va almacenar los estudiante
    estudiantes = []

    funcion_mostrar_encabezado("Bienvenido al sistema de notas escolares")
    print(" --> REGISTRAR ESTUDIANTES REGULARES Y BECADOS")
    print(" --> INGRESAR CALIFICACIONES")

    funcion_mostrar_linea()         

        #Bucle principal del menu
    ejecutando = True
    while ejecutando:
        try:
            opcion = funcion_mostrar_menu()
            #Estructura de condicionales multiples
            if opcion == 1:
                funcion_registrar_estudiante(estudiantes)
                funcion_pausar()
            elif opcion == 2:
                #funcion_registrar_estudiante_becado(estudiantes)
                print("Opcion 2: Registrar estudiante becado (en desarrollo)")
                funcion_pausar()

        except Exception as e:
            print(f"Error: {e}. Intente nuevamente.")
            funcion_pausar() 

#======================================================
# 8. PUNTO DE ENTRADA DEL PROGRAMA
#======================================================

if __name__ == "__main__":
    """
    Este bloque solo se ejecuta cuando el archivo se corre directamente.
    """
    main() 
    