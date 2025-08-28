#Ejercicio 1 _ Sistema de becas
print("EJERCICIO SISTEMAS DE BECAS")

nombre = input("Ingresa tu nombre y apellido: ")
while nombre == "":
    nombre =  input("No puedes dejarlo vacio. Ingresa tu nombre: ")

edad =  input("Ingresa tu edad: ")
while edad == "":
    edad =  input("No puedes dejarlo vacio. Ingresa tu edad: ")

promedio_correcto = {0,1,2,3,4,5,6,7,8,9,10}
promedio_general = input("Ingresa tu promedio general: ")
while promedio_general == "":
    promedio_general =  input("No puedes dejarlo vacio. Ingresa tu promedio: ")

if promedio_general not in promedio_correcto:
    promedio_general = input("El promedio debe ser del 0 al 10. Ingresa tu promedio nuevamente: ")


ingreso_familiar = input("Ingresa los ingresos familiares mensuales: ")
while ingreso_familiar == "":
    ingreso_familiar=  input("No puedes dejarlo vacio. Ingresa tu ingreso familiar: ")


beca = "No definida"


if(int(ingreso_familiar) >= 600000) or (int(promedio_general) < 6) or (int(edad)< 15 or int(edad) > 100) :
    beca = "Beca rechazada"
elif int(ingreso_familiar) < 300000:
    beca = "Beca completa"
elif int(ingreso_familiar) >= 300000 and int(ingreso_familiar) < 600000:
    beca = "Media beca"

print(" ------------- ")
print("- DATOS: ")
print(f"{nombre}, {edad} años")
print(f"Promedio: {promedio_general}")
print(f"Ingresos: {ingreso_familiar}")
print(f"Resultado: {beca}")
print(" --------------- ")





#Ejercicio 2 _ Gestion de turnos hospitalarios
print("EJERCICIO Gestion de turnos hospitalarios")