# Crear lista de datos (0,1) MAX_BARCOS = 5
# condicion_victoria = MAX_BARCOS == barcos_hundidos

# while de ejecucion de juego 
#    usan datos del usuario por turno
#    imprimir matriz por usuario 
#    ingresa coordenadas 
#    hay colision? contra matriz_datos_rival

# Todos los barcos hundidos - Juego terminado

import random
jugando = True

tablero_numeros = random.sample(range(0,1), 25)
tablero = [tablero_numeros[i:i+5] for i in range(0,25,5)]

def mostrar_tablero(tablero):
    for filas in range(5): 
        for columnas in range(5): 
            print(tablero[filas][columnas], "", end=" ") 
        print() 
    print("\n")

while jugando==True:
    mostrar_tablero(tablero)

