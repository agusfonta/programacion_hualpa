# Crear lista de datos (0,1) MAX_BARCOS = 5
# condicion_victoria = MAX_BARCOS == barcos_hundidos

# while de ejecucion de juego 
#    usan datos del usuario por turno
#    imprimir matriz por usuario 
#    ingresa coordenadas 
#    hay colision? contra matriz_datos_rival

# Todos los barcos hundidos - Juego terminado

import random

# Constantes
TAM_TABLERO = 5
MAX_BARCOS = 5

# Crear tablero vacío
def crear_tablero():
    return [[0 for _ in range(TAM_TABLERO)] for _ in range(TAM_TABLERO)]

# Colocar barcos aleatoriamente en el tablero
def colocar_barcos(tablero):
    barcos_colocados = 0
    while barcos_colocados < MAX_BARCOS:
        fila = random.randint(0, TAM_TABLERO - 1)
        columna = random.randint(0, TAM_TABLERO - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            barcos_colocados += 1

# Mostrar tablero (para jugador) sin mostrar barcos del rival
def mostrar_tablero(tablero, ocultar_barcos=True):
    print("  " + " ".join(str(i) for i in range(TAM_TABLERO)))
    for i, fila in enumerate(tablero):
        fila_mostrar = []
        for casilla in fila:
            if ocultar_barcos and casilla == 1:
                fila_mostrar.append("0")  # No mostrar barcos del rival
            else:
                fila_mostrar.append(str(casilla))
        print(i, " ".join(fila_mostrar))
    print("\n")

# Función para procesar un tiro
def disparar(tablero, fila, columna):
    if tablero[fila][columna] == 1:
        tablero[fila][columna] = "X"  # Barco hundido
        print("¡Impacto!")
        return True
    elif tablero[fila][columna] == 0:
        tablero[fila][columna] = "-"  # Agua
        print("Agua.")
        return False
    else:
        print("Ya disparaste ahí.")
        return False

# Contar barcos restantes
def contar_barcos(tablero):
    return sum(fila.count(1) for fila in tablero)

# --- Configurar tableros ---
tablero_jugador = crear_tablero()
tablero_computadora = crear_tablero()
colocar_barcos(tablero_jugador)
colocar_barcos(tablero_computadora)

# --- Juego por turnos ---
jugando = True
while jugando:
    print("Tu tablero:")
    mostrar_tablero(tablero_jugador, ocultar_barcos=False)
    
    print("Tablero rival:")
    mostrar_tablero(tablero_computadora)
    
    # Turno del jugador
    try:
        fila = int(input("Ingresa la fila (0-4) donde disparar: "))
        columna = int(input("Ingresa la columna (0-4) donde disparar: "))
        if fila < 0 or fila >= TAM_TABLERO or columna < 0 or columna >= TAM_TABLERO:
            print("Coordenadas inválidas. Intenta de nuevo.")
            continue
    except ValueError:
        print("Por favor ingresa un número válido.")
        continue
    
    disparar(tablero_computadora, fila, columna)
    
    # Revisar si el jugador ganó
    if contar_barcos(tablero_computadora) == 0:
        print("¡Ganaste! Todos los barcos enemigos fueron hundidos.")
        jugando = False
        break
    
    # Turno de la computadora (aleatorio)
    while True:
        fila_comp = random.randint(0, TAM_TABLERO - 1)
        columna_comp = random.randint(0, TAM_TABLERO - 1)
        if tablero_jugador[fila_comp][columna_comp] in [0, 1]:
            print(f"Computadora dispara en ({fila_comp},{columna_comp})")
            disparar(tablero_jugador, fila_comp, columna_comp)
            break
    
    # Revisar si la computadora ganó
    if contar_barcos(tablero_jugador) == 0:
        print("¡Perdiste! Todos tus barcos fueron hundidos.")
        jugando = False
