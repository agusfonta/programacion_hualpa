# Ejercicio 2 — Gestión de turnos hospitalarios


nombre = input("Ingrese nombre completo: ")
dni = input("Ingrese DNI sin punto ni espacio: ")

if dni.isdigit() and 7 <= len(dni) <= 8:
    dni_valido = True
else:
    dni_valido = False

if dni_valido:  
    edad = int(input("Ingrese edad: "))
    obra_social = input("¿Tiene obra social? (s/n): ").lower()
    prioridad = int(input("Ingrese prioridad médica (1 = emergencia, 2 = urgente, 3 = control): "))
    
    if prioridad == 1:
        turno = "Asignado inmediatamente a guardia"
    
    elif prioridad == 2:
        if obra_social == "s":
            turno = "En menos de 24 hs"
        else:
            turno = "En 48 hs"
    
    elif prioridad == 3:
        if edad > 65:
            turno = "Preferencial en 72 hs"
        else:
            turno = "Normal en 7 días"
    
    else:
        turno = "Prioridad inválida"

    print("Paciente:", nombre)
    print("-DNI:", dni)
    print("-Edad:", edad)
    print("-Prioridad:", prioridad)
    print("-Turno asignado:", turno)

else:
    dni = input("DNI inválido. Debe contener solo números y tener entre 7 y 8 dígitos. Ingrese nuevamente: ")
