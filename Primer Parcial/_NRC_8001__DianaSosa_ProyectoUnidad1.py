# Suiza tiene uno de los mejores puntajes entre los países con excelente calidad de vida. Este tiene un óptimo sistema de seguridad social. Las ciudades son limpias y administradas eficientemente.
# Switzerland has one of the best scores among the countries with excellent quality of life. This has an optimal system of security social. The cities are clean and managed efficiently.

"""
El mini traductor traduce un párrafo de inglés a español y viceversa, el párrafo debe tener
máximo treinta palabras y tres oraciones para poder así visualizar la traducción.

Autor:
Diana Carolina Sosa Romero

Versión:
VER.1.1
"""
# Declarar la variable diccionario
diccionario = {
    "Suiza": "Switzerland", "es": "is", "uno": "one", "de": "of", "mejores": "best", 
    "países": "countries","en": "in", "Las": "The", "mundo": "world", "los": "the",
    "puntajes": "scores","entre": "among", "con": "with", "excelente": "excellent",
    "calidad": "quality","vida": "life", "Este": "This", "tiene": "has", "un": "an",
    "óptimo": "optimal","sistema": "system", "seguridad": "security", "social": "social",
    "Las": "The", "ciudades": "cities", "son": "are", "limpias": "clean", "y": "and",
    "administradas": "managed", "eficientemente": "efficiently"
}


def traducir_de_esp_ing(palabra):
    """
    Es un procedimiento para traducir una palabra de español a inglés
    Parámetros: 
    -----------
        palabra : string
        valor que contiene una palabra en español

    Retorna
    ----------
    Si retorna valor, si existe en el diccionario la palabra a traducir 
    entonces retorna la palabra en inglés de lo contrario imprime None
    """

    # Variable palabra_sin_punto contiene la palabra pero sin el punto
    palabra_sin_punto = palabra.replace(".", "")
    # Comparamos si el contenido de palabra_sin_punto esta en el diccionario
    if (palabra_sin_punto in diccionario):
        # Comparamos si el valor de palabra es igual al de palabra_sin_punto
        if (palabra == palabra_sin_punto):
            # Retorna el valor de la clave
            return diccionario.get(palabra_sin_punto)
        # Si la palabra tiene un punto
        else:
            # Retorna el valor de la clave con un punto
            return diccionario.get(palabra_sin_punto)+'''.'''
    # Si el valor de palabra_sin_punto no está en el diccionario
    else:
        # Retorna mensaje
        return 'None'


def traducir_de_ing_esp(palabra):
    """
    Es un procedimiento para traducir una palabra de inglés a español
    Parámetros: 
    -----------
        palabra : string
        valor que contiene una palabra en inglés

    Retorna
    ----------
    Si retorna valor, si existe en el diccionario la palabra a traducir 
    entonces retorna la palabra en español de lo contrario imprime None
    """
    
    # Variable palabra_sin_punto contiene la palabra pero sin el punto
    palabra_sin_punto = palabra.replace(".", "")

    # Si la palabra sin punto esta en diccionario
    if (palabra == palabra_sin_punto):
        # Recorrer en diccionario cada clave
        for clave in diccionario.keys():
            # Si palabra sin punto es igual al valor de la clave
            if palabra_sin_punto == diccionario[clave]:
                # Retornar la clave
                return clave
    # Si la palabra con punto esta es el diccionario
    else:
        # Recorrer en diccionario cada clave
        for clave in diccionario.keys():
            # Si palabra con punto es igual al valor de la clave
            if palabra_sin_punto == diccionario[clave]:
                # Retornar clave de la palabra con un punto
                return clave+'''.'''
    # Si la palabra no está en el diccionario mostrar mensaje
    return 'None'


def ingresar_parrafo():
    """
    Es un procedimiento para que el usuario pueda ingresar un párrafo
    Parámetros:
    -----------
    No tiene parámetros de entrada

    Retorna
    ----------
        parrafo : tuple
        valor que contiene al párrafo
    """

    # Ingresar palabras
    parrafo = input("Ingrese el párrafo a traducir: ")
    # Asignar a la variable parrafo el párrafo en forma de tupla
    parrafo = tuple(parrafo.split(' '))
    # Retornar variable parrafo
    return parrafo


def validar_palabras(parrafo):
    """"
    Es un procedimiento para verificar que el párrafo tenga 
    máximo treinta palabras
    Parámetros:
    -----------
        parrafo : tuple
        valor que contiene al párrafo

    Retorna
    ----------
        cumple : bool
        valor que contiene el cumplimiento 
        del límite de palabras
    """

    # Inicializar variable cantidad_de_Palabras con el tamaño de la tupla
    cantidad_palabras = len(parrafo)
    # Si la cantidad de palabras es menor a 30
    if cantidad_palabras <= 30:
        cumple = True
        # Asignar a cumple el valor de True
    else:
        # Asignar a cumple el valor de False
        cumple = False
    # Retornar contenido de cumple 
    return cumple


def validar_oraciones(parrafo):
    """Es un procedimiento para permitir el ingreso de hasta 30 palabras
    Parámetros:
    -----------
        parrafo : tuple
        valor que contiene al párrafo

    Retorna
    ----------
        cumple : bool
        valor que contiene el cumplimiento 
        del límite de oraciones
    """

    # Inicializar variable parrafo con el párrafo en forma de string
    parrafo = str(parrafo)
    # Inicializar cantidad_puntos con la cantidad de puntos del párrafo
    cantidad_puntos = parrafo.count('.')
    # Si el valor de cantidad_puntos es tres
    if cantidad_puntos == 3:
        # Asignar a cumple el valor de True
        cumple = True
    else:
        # Asignar a cumple el valor de False
        cumple = False
    # Retornar contenido de cumple
    return cumple

def validar_opcion(opcion):
    """
    Es un procedimiento para validar que solo ingrese números
    Parámetros:
    -----------
        opcion : string
        valor que contiene la opcion

    Retorna
    ----------
        es_numero : bool
        valor que contiene la comprobación de que sea número
    """
    # Si el contenido de opcion es un número
    if opcion.isdigit():
        # Asignar a es_numero el valor de True
        es_numero = True
    else:
        # Asignar a es_numero el valor de False
        es_numero = False
    # Retornar contenido de es_numero
    return es_numero

if __name__ == '__main__':
# Inicializar variable opcion en cero
    opcion = 0
# Ejecutar mientras ingrese la opción sea diferente a tres
while int(opcion) != 3:
    # Mostrar el menú de opciones
    print("\n Elija una opción")
    print("\n1. Traducir de Español a Inglés \n2. Traducir de Inglés a Español \n3. Salir")
    # Asignar a la variable opcion dato ingresado por teclado
    opcion = input("Elija una opción a realizar ")

    # Ejecutar mientras el valor que retorne la función sea False
    while (validar_opcion(opcion) == False):
        # Asignar a la variable opcion dato ingresado por teclado
        opcion = input("Elija una opción a realizar ")

    # Si ingresa el usuario el uno
    if (int(opcion) == 1):
        # Inicializamos variable parrafo_traducido vacío
        parrafo_traducido = ""
        # Inicializamos variable parrafo con el valor que retorne la función
        parrafo = ingresar_parrafo()
        # Ejecutar mientras las dos funciones retonen False
        while (validar_palabras(parrafo) and validar_oraciones(parrafo) == False):
            # Asignar a variable parrafo el valor que retorna ingresar_parrafo
            parrafo = ingresar_parrafo()
        # Recorrer en parrafo cada palabra
        for palabra in parrafo:
            # Asignar a palabra_traducida la palabra traducida
            palabra_traducida = traducir_de_esp_ing(palabra)
            # Asignar a parrafo_traducido cada palabra traducida con un espacio
            parrafo_traducido += palabra_traducida+" "
        # Imprime el contenido de parrafo_traducido
        print(parrafo_traducido)

    # Si opcion es igual a dos
    elif (int(opcion) == 2):
        # Inicializamos variable parrafo_traducido vacío
        parrafo_traducido = ""
        # Inicializamos variable parrafo con el valor que retorne la función
        parrafo = ingresar_parrafo()
        # Ejecutar mientras las dos funciones retonen False
        while (validar_palabras(parrafo) and validar_oraciones(parrafo) == False):
            # Asignar a variable parrafo el valor que retorna ingresar_parrafo
            parrafo = ingresar_parrafo()
        # Recorrer en parrafo cada palabra
        for palabra in parrafo:
            # Asignar a palabra_traducida la palabra traducida
            palabra_traducida = traducir_de_ing_esp(palabra)
            # Asignar a parrafo_traducido cada palabra traducida con un espacio
            parrafo_traducido += palabra_traducida+" "
        # Imprime el contenido de parrafo_traducido
        print(parrafo_traducido)
