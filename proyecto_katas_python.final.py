"""
PROYECTO LÓGICA: KATAS DE PYTHON
Soluciones de las katas 1 a 34 y 36 a 41.

El enunciado original no incluye la kata 35. Por eso se conserva la
numeración original y no se inventa un ejercicio para ese número.

Para ejecutar:
    python proyecto_katas_python.py

El programa ejecuta automáticamente las pruebas de ejemplo. Los ejercicios
que normalmente piden datos por teclado tienen también funciones auxiliares
que permiten probarlos sin detener la ejecución automática.
"""

from functools import reduce
import math


# ============================================================
# KATAS 1 A 5: FUNCIONES Y ESTRUCTURAS DE DATOS
# ============================================================

# KATA 1
def contar_frecuencias(texto):
    """Devuelve un diccionario con la frecuencia de cada carácter, sin espacios."""
    frecuencias = {}

    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1

    return frecuencias


# KATA 2
def duplicar_numeros(numeros):
    """Devuelve una lista con cada número multiplicado por dos."""
    return list(map(lambda numero: numero * 2, numeros))


# KATA 3
def palabras_que_contienen(lista_palabras, objetivo):
    """Devuelve las palabras que contienen el texto objetivo."""
    return [palabra for palabra in lista_palabras if objetivo in palabra]


# KATA 4
def diferencias_listas(lista1, lista2):
    """Resta los elementos de la segunda lista a los de la primera, posición a posición."""
    return list(map(lambda a, b: a - b, lista1, lista2))


# KATA 5
def calcular_estado(notas, nota_aprobado=5):
    """Calcula la media y devuelve una tupla con la media y el estado."""
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")

    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"

    return media, estado


# ============================================================
# KATAS 6 A 11: RECURSIVIDAD Y EXCEPCIONES
# ============================================================

# KATA 6
def factorial(numero):
    """Calcula el factorial de un entero no negativo mediante recursividad."""
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("El factorial requiere un número entero.")
    if numero < 0:
        raise ValueError("No existe factorial para números negativos.")

    # Caso base: 0! y 1! valen 1. Detiene las llamadas recursivas.
    if numero <= 1:
        return 1

    # Caso recursivo: el problema se reduce al factorial del número anterior.
    return numero * factorial(numero - 1)


# KATA 7
def tuplas_a_strings(lista_tuplas):
    """Convierte cada tupla en una cadena de texto."""
    return list(map(lambda tupla: str(tupla), lista_tuplas))


# KATA 8
def dividir(numero1, numero2):
    """Realiza una división y devuelve un mensaje si ocurre un error."""
    try:
        resultado = float(numero1) / float(numero2)
        return f"División exitosa: {resultado}"
    except ValueError:
        return "Error: se deben introducir valores numéricos."
    except ZeroDivisionError:
        return "Error: no se puede dividir por cero."


def programa_division():
    """Solicita dos números al usuario y muestra el resultado de la división."""
    numero1 = input("Introduce el primer número: ")
    numero2 = input("Introduce el segundo número: ")
    print(dividir(numero1, numero2))


# KATA 9
def filtrar_mascotas_permitidas(mascotas):
    """Elimina de la lista las mascotas incluidas en la lista de prohibidas."""
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda mascota: mascota not in prohibidas, mascotas))


# KATA 10
class ListaVaciaError(Exception):
    """Excepción personalizada para indicar que una lista está vacía."""
    pass


def promedio_con_excepcion(numeros):
    """Calcula el promedio o lanza una excepción si la lista está vacía."""
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")

    return sum(numeros) / len(numeros)


# KATA 11
def validar_edad(valor):
    """Convierte y valida una edad. Devuelve la edad como entero."""
    try:
        edad = int(valor)
    except ValueError:
        raise ValueError("La edad debe ser un número entero.")

    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120.")

    return edad


def solicitar_edad():
    """Solicita una edad por teclado y gestiona los errores."""
    try:
        edad = validar_edad(input("Introduce tu edad: "))
        print(f"Edad válida: {edad}")
    except ValueError as error:
        print(f"Error: {error}")


# ============================================================
# KATAS 12 A 27: PROGRAMACIÓN FUNCIONAL Y LAMBDAS
# ============================================================

# KATA 12
def longitudes_palabras(frase):
    """Devuelve una lista con la longitud de cada palabra de la frase."""
    palabras = frase.split()
    return list(map(len, palabras))


# KATA 13
def pares_mayusculas_minusculas(caracteres):
    """Devuelve tuplas (mayúscula, minúscula), sin repetir caracteres."""
    caracteres_unicos = list(dict.fromkeys(caracteres))
    return list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos))


# KATA 14
def palabras_que_empiezan_con(palabras, letra):
    """Filtra las palabras que comienzan con la letra indicada."""
    return list(filter(lambda palabra: palabra.startswith(letra), palabras))


# KATA 15
sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# KATA 16
def palabras_mas_largas_que(texto, n):
    """Devuelve las palabras cuya longitud es mayor que n."""
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# KATA 17
def digitos_a_numero(digitos):
    """Convierte una lista de dígitos en el número entero correspondiente."""
    if not digitos:
        raise ValueError("La lista de dígitos no puede estar vacía.")

    if any(not isinstance(d, int) or isinstance(d, bool) or d < 0 or d > 9
           for d in digitos):
        raise ValueError("Todos los elementos deben ser dígitos enteros entre 0 y 9.")

    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos, 0)


# KATA 18
def estudiantes_aprobados(estudiantes):
    """Devuelve los estudiantes cuya calificación es mayor o igual a 90."""
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


# KATA 19
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# KATA 20
def obtener_enteros(elementos):
    """Devuelve únicamente los valores int; excluye bool, aunque sea subtipo de int."""
    return list(filter(lambda elemento: isinstance(elemento, int)
                       and not isinstance(elemento, bool), elementos))


# KATA 21
cubo = lambda numero: numero ** 3


# KATA 22
def producto_total(numeros):
    """Multiplica todos los elementos de la lista."""
    return reduce(lambda acumulado, numero: acumulado * numero, numeros, 1)


# KATA 23
def concatenar_palabras(palabras):
    """Une todas las palabras de una lista en una sola cadena, sin separador."""
    return reduce(lambda acumulado, palabra: acumulado + palabra, palabras, "")


# KATA 24
def diferencia_total(numeros):
    """Resta sucesivamente los elementos a partir del primero."""
    if not numeros:
        return 0

    return reduce(lambda acumulado, numero: acumulado - numero, numeros)


# KATA 25
def contar_caracteres(texto):
    """Devuelve el número de caracteres de una cadena, incluidos los espacios."""
    return len(texto)


# KATA 26
resto_division = lambda numero1, numero2: numero1 % numero2


# KATA 27
def promedio(numeros):
    """Calcula el promedio de una lista de números."""
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")

    return sum(numeros) / len(numeros)


# ============================================================
# KATAS 28 A 33: BÚSQUEDA Y MANIPULACIÓN DE DATOS
# ============================================================

# KATA 28
def primer_duplicado(elementos):
    """Devuelve el primer elemento que aparece por segunda vez."""
    vistos = set()

    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None


# KATA 29
def enmascarar_texto(valor):
    """Enmascara todos los caracteres salvo los últimos cuatro."""
    texto = str(valor)

    if len(texto) <= 4:
        return texto

    return "#" * (len(texto) - 4) + texto[-4:]


# KATA 30
def son_anagramas(palabra1, palabra2):
    """Comprueba si dos palabras contienen las mismas letras."""
    normalizada1 = palabra1.replace(" ", "").lower()
    normalizada2 = palabra2.replace(" ", "").lower()

    return sorted(normalizada1) == sorted(normalizada2)


# KATA 31
def buscar_nombre(nombres, nombre_buscado):
    """Busca un nombre en una lista o lanza una excepción si no está."""
    if nombre_buscado in nombres:
        return f"{nombre_buscado} fue encontrado."
    raise LookupError(f"{nombre_buscado} no está en la lista.")


def programa_buscar_nombre():
    """Pide una lista de nombres y luego solicita un nombre para buscar."""
    nombres = input("Introduce nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre_buscado = input("¿Qué nombre quieres buscar?: ").strip()

    try:
        print(buscar_nombre(nombres, nombre_buscado))
    except LookupError as error:
        print(f"Error: {error}")


# KATA 32
def buscar_puesto(nombre_completo, empleados):
    """Busca el puesto de una persona en una lista de empleados."""
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]

    return "La persona no trabaja aquí."


# KATA 33
sumar_listas = lambda lista1, lista2: list(map(lambda a, b: a + b, lista1, lista2))


# ============================================================
# KATAS 34 Y 36: PROGRAMACIÓN ORIENTADA A OBJETOS
# La kata 35 no aparece en el enunciado original.
# ============================================================

# KATA 34
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama indicada usando índices de Python (comienzan en 0)."""
        if not isinstance(posicion, int) or isinstance(posicion, bool):
            raise TypeError("La posición debe ser un número entero.")
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError("No existe una rama en esa posición.")

        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy()
        }


# KATA 36
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")

        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Retira dinero si hay cuenta corriente y saldo suficiente."""
        if not self.cuenta_corriente:
            raise PermissionError("El usuario no tiene cuenta corriente.")
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= cantidad
        return self.saldo

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro_usuario hacia el usuario actual."""
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise PermissionError("Ambos usuarios deben tener cuenta corriente.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > otro_usuario.saldo:
            raise ValueError("El usuario que envía no tiene saldo suficiente.")

        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        return self.saldo

    def agregar_dinero(self, cantidad):
        """Agrega dinero al saldo del usuario."""
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")

        self.saldo += cantidad
        return self.saldo


# ============================================================
# KATAS 37 A 41: TEXTO, CONDICIONALES Y CÁLCULOS
# ============================================================

# KATA 37
def contar_palabras(texto):
    """Cuenta cuántas veces aparece cada palabra (sin distinguir mayúsculas)."""
    frecuencias = {}

    for palabra in texto.lower().split():
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1

    return frecuencias


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza todas las apariciones de una palabra por otra."""
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra):
    """Elimina las apariciones de una palabra del texto."""
    return " ".join(
        elemento for elemento in texto.split()
        if elemento != palabra
    )


def procesar_texto(texto, opcion, *argumentos):
    """
    Procesa un texto según la opción elegida:
    contar, reemplazar o eliminar.
    """
    if opcion == "contar":
        if argumentos:
            raise ValueError("La opción 'contar' no necesita argumentos adicionales.")
        return contar_palabras(texto)

    if opcion == "reemplazar":
        if len(argumentos) != 2:
            raise ValueError("Para reemplazar se necesitan palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])

    if opcion == "eliminar":
        if len(argumentos) != 1:
            raise ValueError("Para eliminar se necesita una palabra.")
        return eliminar_palabra(texto, argumentos[0])

    raise ValueError("Opción no válida. Usa: contar, reemplazar o eliminar.")


# KATA 38
def momento_del_dia(hora):
    """Indica si la hora corresponde a noche, día o tarde."""
    if not isinstance(hora, int) or isinstance(hora, bool) or hora < 0 or hora > 23:
        raise ValueError("La hora debe ser un entero entre 0 y 23.")

    if hora < 6 or hora >= 20:
        return "noche"
    elif hora < 12:
        return "día"
    else:
        return "tarde"


def programa_momento_del_dia():
    """Solicita una hora por teclado e informa el momento del día."""
    try:
        hora = int(input("Introduce la hora (0-23): "))
        print(f"Es de {momento_del_dia(hora)}.")
    except ValueError as error:
        print(f"Error: {error}")


# KATA 39
def calificacion_texto(calificacion):
    """Convierte una calificación numérica en una calificación textual."""
    if not isinstance(calificacion, (int, float)) or isinstance(calificacion, bool):
        raise TypeError("La calificación debe ser numérica.")
    if calificacion < 0 or calificacion > 100:
        raise ValueError("La calificación debe estar entre 0 y 100.")

    if calificacion < 70:
        return "insuficiente"
    elif calificacion < 80:
        return "bien"
    elif calificacion < 90:
        return "muy bien"
    else:
        return "excelente"


# KATA 40
def calcular_area(figura, datos):
    """Calcula el área de un rectángulo, círculo o triángulo."""
    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2

    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    else:
        raise ValueError("Figura no válida. Usa rectangulo, circulo o triangulo.")


# KATA 41
def calcular_compra(precio, tiene_cupon, descuento=0):
    """Calcula el precio final aplicando un descuento válido en euros."""
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

    if tiene_cupon and descuento > 0:
        precio_final = precio - descuento
        # El precio final nunca puede ser inferior a cero.
        return max(precio_final, 0)

    return precio


def programa_compra():
    """Solicita los datos de una compra y muestra el precio final."""
    try:
        precio = float(input("Introduce el precio original: "))
        respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if respuesta in ("si", "sí"):
            descuento = float(input("Introduce el valor del descuento en euros: "))
            if descuento > 0:
                precio_final = calcular_compra(precio, True, descuento)
                print(f"Precio final con descuento: {precio_final:.2f} €")
            else:
                print(f"Cupón no válido. Precio final: {precio:.2f} €")
        elif respuesta == "no":
            print(f"Precio final: {precio:.2f} €")
        else:
            print("Respuesta no válida. Escribe sí o no.")

    except ValueError as error:
        print(f"Error: {error}")


# ============================================================
# PRUEBAS AUTOMÁTICAS DE TODAS LAS KATAS
# ============================================================

def ejecutar_pruebas():
    """Ejecuta ejemplos de las katas sin solicitar datos por teclado."""
    print("\n" + "=" * 60)
    print("PROYECTO LÓGICA: KATAS DE PYTHON")
    print("=" * 60)

    print("\n--- KATAS 1 A 5 ---")
    print("Kata 1:", contar_frecuencias("hola mundo"))
    print("Kata 2:", duplicar_numeros([1, 2, 3]))
    print("Kata 3:", palabras_que_contienen(["casa", "casamiento", "perro"], "casa"))
    print("Kata 4:", diferencias_listas([10, 8, 6], [1, 2, 3]))
    print("Kata 5:", calcular_estado([7, 8, 6]))

    print("\n--- KATAS 6 A 11 ---")
    print("Kata 6:", factorial(5))
    print("Kata 7:", tuplas_a_strings([("Ana", 20), ("Luis", 22)]))
    print("Kata 8:", dividir("10", "2"))
    print("Kata 8 (error controlado):", dividir("10", "0"))
    print("Kata 9:", filtrar_mascotas_permitidas(
        ["Perro", "Mapache", "Gato", "Oso"]
    ))
    try:
        print("Kata 10:", promedio_con_excepcion([4, 6, 8]))
        promedio_con_excepcion([])
    except ListaVaciaError as error:
        print("Kata 10 (excepción controlada):", error)
    try:
        print("Kata 11:", validar_edad("34"))
        validar_edad("150")
    except ValueError as error:
        print("Kata 11 (validación controlada):", error)

    print("\n--- KATAS 12 A 20 ---")
    print("Kata 12:", longitudes_palabras("Python es interesante"))
    print("Kata 13:", pares_mayusculas_minusculas("abca"))
    print("Kata 14:", palabras_que_empiezan_con(["casa", "perro", "coche"], "c"))
    print("Kata 15:", sumar_tres([1, 2, 3]))
    print("Kata 16:", palabras_mas_largas_que("Python es muy interesante", 4))
    print("Kata 17:", digitos_a_numero([5, 7, 2]))
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 85},
        {"nombre": "Marta", "edad": 21, "calificacion": 90},
    ]
    print("Kata 18:", estudiantes_aprobados(estudiantes))
    print("Kata 19:", filtrar_impares([1, 2, 3, 4, 5]))
    print("Kata 20:", obtener_enteros([1, "dos", 3, "cuatro", True]))

    print("\n--- KATAS 21 A 27 ---")
    print("Kata 21:", cubo(3))
    print("Kata 22:", producto_total([2, 3, 4]))
    print("Kata 23:", concatenar_palabras(["Hola", " ", "mundo"]))
    print("Kata 24:", diferencia_total([20, 5, 3]))
    print("Kata 25:", contar_caracteres("Hola mundo"))
    print("Kata 26:", resto_division(10, 3))
    print("Kata 27:", promedio([10, 8, 6]))

    print("\n--- KATAS 28 A 33 ---")
    print("Kata 28:", primer_duplicado([1, 2, 3, 2, 4]))
    print("Kata 29:", enmascarar_texto("123456789"))
    print("Kata 30:", son_anagramas("Roma", "Amor"))
    print("Kata 31:", buscar_nombre(["Ana", "Luis", "Marta"], "Luis"))
    empleados = [
        {"nombre": "Ana Pérez", "puesto": "Analista"},
        {"nombre": "Luis Gómez", "puesto": "Desarrollador"},
    ]
    print("Kata 32:", buscar_puesto("Ana Pérez", empleados))
    print("Kata 33:", sumar_listas([1, 2, 3], [4, 5, 6]))

    print("\n--- KATAS 34 Y 36 ---")
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print("Kata 34:", arbol.info_arbol())

    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    # El enunciado tiene una inconsistencia: Bob empieza con 50 y recibe 20,
    # por lo que dispone de 70; no puede transferir 80 sin quedar en negativo.
    try:
        alicia.transferir_dinero(bob, 80)
    except ValueError as error:
        print("Kata 36 - transferencia de 80 no realizada:", error)

    # La ejecución continúa y Alicia puede retirar 50 de su saldo inicial.
    alicia.retirar_dinero(50)
    print("Kata 36 - saldo Alicia:", alicia.saldo)
    print("Kata 36 - saldo Bob:", bob.saldo)

    print("\n--- KATAS 37 A 41 ---")
    texto = "Python es fácil y Python es útil"
    print("Kata 37 (contar):", procesar_texto(texto, "contar"))
    print("Kata 37 (reemplazar):", procesar_texto(texto, "reemplazar", "fácil", "potente"))
    print("Kata 37 (eliminar):", procesar_texto(texto, "eliminar", "útil"))
    print("Kata 38:", momento_del_dia(15))
    print("Kata 39:", calificacion_texto(92))
    print("Kata 40 - rectángulo:", calcular_area("rectangulo", (5, 3)))
    print("Kata 40 - círculo:", round(calcular_area("circulo", (2,)), 2))
    print("Kata 40 - triángulo:", calcular_area("triangulo", (5, 3)))
    print("Kata 41:", calcular_compra(100, True, 15))

    print("\n" + "=" * 60)
    print("FIN DE LAS PRUEBAS AUTOMÁTICAS")
    print("Las katas 8, 11, 31, 38 y 41 también tienen")
    print("funciones interactivas para probar entradas por teclado:")
    print("programa_division(), solicitar_edad(), programa_buscar_nombre(),")
    print("programa_momento_del_dia() y programa_compra().")
    print("=" * 60)


# Este bloque hace que las pruebas se ejecuten al lanzar este archivo.
# Si el archivo se importa desde otro programa, las pruebas no se ejecutan.
if __name__ == "__main__":
    ejecutar_pruebas()
