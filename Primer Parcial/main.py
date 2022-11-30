# Importar módulo traductor
import traductor 
# Inicializar variable opcion en cero
opcion = 0
# Ejecutar mientras ingrese la opción sea diferente a tres
while opcion != 3:
    # Mostrar mensaje
    print("\n Elija una opción")
    print("\n1. Traducir de ESPAÑOL-INGLÉS \n2. Traducir de INGLÉS-ESPAÑOL \n3. Salir")
    # Asignar a la variable opcion dato ingresado por teclado
    opcion = int(input("Elija una opción a realizar "))
    # Si ingresa el usuario el uno
    if (opcion == 1):
        # Inicializar variable parrafo_Traducido vacía
        parrafo_Traducido = ""
        # Inicializar variable formacion_Parrafo con párrafo en forma de tupla
        formacion_Parrafo = traductor.ingresar_Parrafo()
        # Ejecutar mientras sea verdadero
        while(True):
            # Si el párrafo cumple con el límite de palabras y oraciones
            if(traductor.validarParrafo_Palabras(formacion_Parrafo) and traductor.validarParrafo_Oraciones(formacion_Parrafo)):
                # Recorrer en formacion_Parrafo cada palabra del párrafo
                for termino in formacion_Parrafo:
                    # Asignar a palabra_Traducida la palabra traducida
                    palabra_Traducida = traductor.Traducir_de_ESP_ING(termino)
                    # Asignar a parrafo_Traducido cada palabra traducida con un espacio
                    parrafo_Traducido += palabra_Traducida+" "
                # Parar
                break
            # Si el párrafo no cumple con el límite de palabras y oraciones
            else:
                # Asignar a variable formacion_Parrafo el nuevo párrafo
                formacion_Parrafo = traductor.ingresar_Parrafo()
        # Mostrar párrafo traducido de español a inglés
        print(parrafo_Traducido)

    # Si ingresa el usuario el dos
    elif (opcion == 2):
        # Inicializar variable parrafo_Traducido vacía
        parrafo_Traducido = ""
        # Inicializar variable formacion_Parrafo con párrafo en forma de tupla
        formacion_Parrafo = traductor.ingresar_Parrafo()
        # Ejecutar mientras sea verdadero
        while(True):
            # Si el párrafo cumple con el límite de palabras y oraciones
            if(traductor.validarParrafo_Palabras(formacion_Parrafo) and traductor.validarParrafo_Oraciones(formacion_Parrafo)):
                # Recorrer en formacion_Parrafo cada palabra del párrafo
                for termino in formacion_Parrafo:
                    # Asignar a palabra_Traducida la palabra traducida
                    palabra_Traducida = traductor.Traducir_de_ING_ESP(termino)
                    # Asignar a parrafo_Traducido cada palabra traducida con un espacio
                    parrafo_Traducido += palabra_Traducida+" "
                # Parar
                break
            # Si el párrafo no cumple con el límite de palabras y oraciones
            else:
                # Asignar a variable formacion_Parrafo el nuevo párrafo
                formacion_Parrafo = traductor.ingresar_Parrafo()
        # Mostrar párrafo traducido de inglés a español
        print(parrafo_Traducido)

