import random

# Lista de alumnos
lista_alumnos = [
    "Lautaro Agustín Aguero",
    "Mateo Alejo Algañaraz",
    "Yoselie Aquino",
    "Santiago Facundo Barretto",
    "Ayrton Calderon",
    "María Belén Calvo García",
    "Nicolas Exequiel Carchano",
    "Sergio Joaquin Chiarello Ghilardi",
    "Santino Cárdenas Valls",
    "Octavio Agustin Fiore Montivero",
    "Bruno Fiouchetta",
    "Braian Leandro Flores Marin",
    "Agustina Luz Fontagnol",
    "Maximo Mateo Franco",
    "Facundo Adrian Gomez Romero",
    "Marcelo Hernán Gonzalez",
    "Genaro Guillot",
    "Camilo Javier Illanes Donoso",
    "Matias Nicolas Limina Nuñez",
    "Federico Alejandro Lopez",
    "Jeremías Daniel Luzuriaga",
    "Santino Mantineo",
    "Ezequiel Menéndez",
    "Nicolás Monjelardi",
    "Joel Nicolas Moreno",
    "Nicolás Uriel Moron Gutierrez",
    "Joaquín Morán",
    "Santino Naldini Sosa",
    "Andres Victor Novello",
    "Joseph Oliveros",
    "Santiago Javier Ontivero Parlade",
    "Roberto Paul Paiva",
    "Matías Pereyra",
    "Gianella Sol Peña",
    "Leonel Lautaro Ponce De Leon Martinez",
    "Cristian Nestor Rodriguez Martinez",
    "Ignacio Martín Rodríguez",
    "Rafael Ignacio Ruiz Guiñazú Puebla",
    "Florencia Santos",
    "Marcelo Scherer Huf",
    "Martina Guadalupe Suarez",
    "Elias Emanuel Tello",
    "Agustina Luz Fontagnol"
]

random.shuffle(lista_alumnos)

tamaño_grupo = 4

total_alumnos = len(lista_alumnos)
cantidad_grupos = total_alumnos // tamaño_grupo
alumnos_sobrantes = total_alumnos % tamaño_grupo

lista_grupos = []

indice_inicio = 0
for i in range(cantidad_grupos):
    indice_fin = indice_inicio + tamaño_grupo + (1 if alumnos_sobrantes > 0 else 0)
    grupo_actual = lista_alumnos[indice_inicio:indice_fin]
    lista_grupos.append(grupo_actual)
    indice_inicio = indice_fin
    if alumnos_sobrantes > 0:
        alumnos_sobrantes -= 1

for numero_grupo, grupo in enumerate(lista_grupos, start=1):
    print(f"Grupo {numero_grupo}: {grupo}")
