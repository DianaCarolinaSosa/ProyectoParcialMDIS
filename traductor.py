# Suiza tiene uno de los mejores puntajes entre los países con excelente calidad de vida. Este tiene un óptimo sistema de seguridad social. Las ciudades son limpias y administradas eficientemente.
# Switzerland has one of the best scores among the countries with excellent quality of life. This has an optimal system of security social. The cities are clean and managed efficiently.

# Declarar la variable diccionario
diccionario = {
    "Suiza":"Switzerland", "es":"is","uno": "one","de":"of","mejores":"best","países":"countries",
    "en" :"in","Las":"The", "mundo":"world","los":"the","puntajes":"scores",
    "entre":"among", "con":"with","excelente":"excellent","calidad":"quality",
    "vida":"life","Este":"This","tiene":"has","un" :"an","óptimo":"optimal",
    "sistema":"system","seguridad":"security","social":"social",
    "Las":"The", "ciudades":"cities", "son":"are" ,"limpias":"clean","y":"and",
    "administradas":"managed","eficientemente":"efficiently"
}


def Traducir_de_ESP_ING(texto):

    # Es un procedimiento para traducir palabras de español a inglés
    # Parámetros: 
    # -----------
    # variable texto es tipo cadena de caracteres

    # Retorna
    # ----------
    # retorna cadena de caracteres

    # Variable nuevo_Texto elimina los puntos del la palabra 
    nuevo_Texto = texto.replace(".", "")
    # Si la palabra sin punto esta en diccionario
    if(nuevo_Texto in diccionario):
        # Si la palabra no tiene punto
        if(texto==nuevo_Texto):
            # Retorna contenido de la llave
            return diccionario.get(nuevo_Texto)
        # Si la palabra tiene punto
        else:
            # Retorna contenido de la llave con un punto
            return diccionario.get(nuevo_Texto)+'''.'''
    # Si la palabra no está en el diccionario
    else:
        # Retorna mensaje
        return 'None'

def Traducir_de_ING_ESP(texto):

    # Es un procedimiento para traducir palabras de inglés a español
    # Parámetros: 
    # -----------
    # variable texto es tipo cadena de caracteres

    # Retorna
    # ----------
    # cadena de caracteres

    # Variable nuevo_Texto elimina los puntos del la palabra 
    nuevo_Texto = texto.replace(".", "")
    
    # Si la palabra sin punto esta en diccionario
    if(texto==nuevo_Texto):
        # Recorrer en diccionario cada llave
        for llave in diccionario.keys():
            # Si palabra sin punto es igual al contenido de la llave
            if nuevo_Texto == diccionario[llave]:
            # Retornar llave de la palabra
             return llave
    # Si la palabra con punto esta es el diccionario
    else:
        # Recorrer en diccionario cada llave
        for llave in diccionario.keys():
            # Si palabra con punto es igual al contenido de la llave
            if nuevo_Texto == diccionario[llave]:
            # Retornar llave de la palabra con un punto
             return llave+'''.'''
    # Si la palabra no está en el diccionario mostrar mensaje
    return 'None' 


def ingresar_Parrafo():
    # Es un procedimiento para convertir las palabras en párrafo
    # Parámetros: 
    # -----------
    # No tiene parámetros de entrada

    # Retorna
    # ----------
    # variable parrafo_Tupla es tipo tupla

    # Inicializar variable parrafo vacío
    parrafo = ""
    # Ingresar palabras
    palabra = input("Escriba el párrafo a traducir ")
    # Juntar palabras en un párrafo
    parrafo += palabra
    # Asignar a la variable parrafo_Tupla el párrafo en forma de tupla
    parrafo_Tupla = tuple(parrafo.split(' '))
    # Retornar variable parrafo_Tupla
    return parrafo_Tupla


def validarParrafo_Palabras(nuevo_Parrafo):
    # Es un procedimiento para permitir el ingreso de hasta 30 palabras
    # Parámetros: 
    # -----------
    # variable nuevo_Parrafo es tipo tupla

    # Retorna
    # ----------
    # bool

    # Inicializar variable cantidad_de_Palabras con el tamaño de la tupla
    cantidad_de_Palabras = len(nuevo_Parrafo)
    # Si la cantidad de palabras es menor a 30
    if cantidad_de_Palabras <= 30:
        # Retornar verdadero
        return True


def validarParrafo_Oraciones(nuevo_Parrafo):
    # Es un procedimiento para permitir el ingreso de hasta 30 palabras
    # Parámetros: 
    # -----------
    # variable nuevo_Parrafo es tipo tupla

    # Retorna
    # ----------
    # bool

    # Inicializa variable cadena_Lista con el párrafo
    cadena_Lista = str(nuevo_Parrafo)
    # Inicializa variable numero_de_Puntos con la cantidad de puntos del párrafo
    numero_de_Puntos = cadena_Lista.count('.')
    # Si la cantidad números del párrafo es tres
    if numero_de_Puntos == 3:
        # Retornar veradero
        return True
