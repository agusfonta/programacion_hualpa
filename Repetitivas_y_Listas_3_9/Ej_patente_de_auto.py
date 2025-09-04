## Ejercicio Patentes 

import re

LETRAS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

PATENTE_VIEJA = re.compile(r"^[A-Z]{3}\s?[0-9]{3}$", re.IGNORECASE)
#Verifica el formato de AAA OOO

def validar_patente_vieja(patente: str) -> bool:
    return bool(PATENTE_VIEJA.fullmatch(patente.strip()))
#Devuelve True o False si coincide o no con el patron de patente

def normalizar_patente(patente: str) -> str:
    return patente.replace(" ", "").upper()
#Eliminamos todos los espacios y convertimos todo en Mayusculas

entrada = input("Ingrese una patente (ej: AAA 000): ")
terminar_programa = False

while not validar_patente_vieja(entrada):
    entrada = input("Patente inválida. Ingrese nuevamente: ")
else:
    patente = normalizar_patente(entrada)
    print(f"Patente válida: {patente}")
    incremento = int(input("Ingresa el número de patentes que quieres ver hacia adelante: "))
    #EJ si incremento es 2 y la patente es AAA 998. El resultado seria patente AAB 000

    # Separar letras y números
    letra1 = patente[0]
    letra2 = patente[1]
    letra3 = patente[2]
    numeros = int(patente[3:])

    # Lógica de incremento si es mínimo
    numeros += incremento

    # Lógica de incremento si supera los 999
    while numeros > 999:
        numeros -= 1000  # Pasamos a la siguiente letra
        # Incrementa letra3
        posicion_l3 = LETRAS.index(letra3) + 1
        if posicion_l3 >= len(LETRAS):
            letra3 = LETRAS[0]
            # Incrementa letra2
            posicion_l2 = LETRAS.index(letra2) + 1
            if posicion_l2 >= len(LETRAS):
                letra2 = LETRAS[0]
                # Incrementa letra1
                posicion_l1 = LETRAS.index(letra1) + 1
                if posicion_l1 >= len(LETRAS):
                    letra1 = LETRAS[0]
                    #Si la letra llega a Z significa que no es mas valida la patente 
                    #Seria ZZZ 999
                    #terminamos el programa imprimiendo el if de mas abajo
                    terminar_programa = True
                    break
                else:
                    letra1 = LETRAS[posicion_l1]
            else:
                letra2 = LETRAS[posicion_l2]
        else:
            letra3 = LETRAS[posicion_l3]

    numeros_formateados = f"{numeros:03d}"
    # Los deja con 3 cifras ej 1 queda 001

    if terminar_programa:
        print("Has superado el número de patentes posibles")
    else:
        print(f"PATENTE RESULTADO: {letra1}{letra2}{letra3} {numeros_formateados}")

