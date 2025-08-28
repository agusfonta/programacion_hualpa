# Ejercicio 3 — Evaluación de crédito bancario


nombre = input("Ingrese nombre y apellido: ")

cuit_valido = False
while not cuit_valido:
    cuit = input("Ingrese CUIT (ej: 20-30233444-9): ")

    cuit_sin_guiones = cuit.replace("-", "")
    if cuit_sin_guiones.isdigit() and len(cuit_sin_guiones) == 11:
        cuit_valido = True
    else:
        print("CUIT inválido. Debe tener 11 dígitos (puede incluir guiones). Intente de nuevo.")

ingresos = int(input("Ingrese ingresos mensuales: $"))
antiguedad = int(input("Ingrese antigüedad laboral (en años): "))
historial = input("Ingrese historial crediticio (bueno/regular/malo): ").lower()


if historial == "malo":
    monto = 0   
elif ingresos < 200000:
    monto = 0   
else:
    if antiguedad < 2:
        monto = 500000
    else:
        if historial == "regular":
            monto = 1000000
        elif historial == "bueno":
            monto = 3000000
        else:
            monto = 0  


print("-----------------------------------")
print(f"Cliente: {nombre}")
print(f"-CUIT: {cuit}")
print(f"-Ingresos: ${ingresos}")
print(f"-Antigüedad: {antiguedad} años")
print(f"-Historial: {historial}")

if monto == 0:
    print(" Crédito rechazado")
else:
    print(f"Monto aprobado: ${monto:,}")
print("-----------------------------------")
