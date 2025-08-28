# Ejercicio 1 - Clasificación de impuestos
print(f" \n EJERCICIO 1 - CLASIFICACION DE IMPUESTOS \n ")

nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos anuales sin punto ni coma: $"))

if ingresos < 500000:
    impuesto = 0
elif  500000 <= ingresos < 2000000:
    impuesto = ingresos * 0.10
elif  2000000 <= ingresos < 5000000:
    impuesto = ingresos * 0.20
else:
    impuesto = ingresos * 0.35

if edad > 65:
    impuesto = impuesto / 2

print(f"\n-Nombre: {nombre}")
print(f"-Edad: {edad}")
print(f"-Ingresos anuales: ${ingresos:,.2f}")
print(f"-Impuesto final: ${impuesto:,.2f}")

# Ejercicio 2 - Sistema de calificaciones
print(f" \n EJERCICIO 2 - Sistema de calificaciones \n ")

nombre = input("Ingrese nombre del alumno: ")
legajo = input("Ingrese legajo: ")
nota1 = int(input("Ingrese nota 1 (0-10): "))
nota2 = int(input("Ingrese nota 2 (0-10): "))
nota3 = int(input("Ingrese nota 3 (0-10): "))

promedio = (nota1 + nota2 + nota3) / 3

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    estado = "Desaprobado directo"
elif promedio < 6:
    estado = "Desaprobado"
elif promedio < 8:
    estado = "Aprobado con final"
else:
    estado = "Promocionado"

print(f"\nAlumno: {nombre} (Legajo {legajo})")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado académico: {estado}")

# Ejercicio 3 - Cajero automático
print(f" \n EJERCICIO 3 - Cajero automatico \n ")

usuario = input("Ingrese su nombre: ")
pin_correcto = "1234"
saldo = 50000
intentos = 0
validado = False

while intentos < 3 and not validado:
    pin = input("Ingrese su PIN: ")
    if pin == pin_correcto:
        validado = True
    else:
        intentos += 1
        print("PIN incorrecto.")

if not validado:
    print("Demasiados intentos. Tarjeta bloqueada.")
else:
    while True:
        monto = input("\nIngrese monto a retirar (o escriba 'cancelar'): ")
        if monto.lower() == "cancelar":
            print("Operación cancelada.")
            break

        monto = int(monto)

        if monto % 1000 != 0:
            print("El monto debe ser múltiplo de 1000.")
        elif monto > saldo:
            print("Saldo insuficiente.")
        else:
            comision = 0
            if monto > 20000:
                comision = monto * 0.02
            total = monto + comision
            saldo -= total
            print(f"Retiro: ${monto}")
            print(f"Comisión: ${comision:.2f}")
            print(f"Saldo restante: ${saldo:.2f}")
            break


# Ejercicio 4 - Categoría de conductores
print(f" \n EJERCICIO 4 - Categoría de conductores  \n ")


nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
experiencia = int(input("Ingrese años de experiencia: "))

if edad < 18:
    categoria = "No puede conducir"
elif edad >= 30 and experiencia > 10:
    categoria = "Conductor profesional"
elif edad >= 21 and 1 <= experiencia <= 5:
    categoria = "Conductor intermedio"
elif edad >= 18 and experiencia < 1:
    categoria = "Principiante"
else:
    categoria = "Conductor estándar"

print(f"\nConductor: {nombre}")
print(f"Edad: {edad} años - Experiencia: {experiencia} años")
print(f"Categoría asignada: {categoria}")

# Ejercicio 5 - Carrito de compras
print(f" \n EJERCICIO 5 - Carrito de compras  \n ")

cliente = input("Ingrese nombre del cliente: ")
cantidad = int(input("Ingrese cantidad de productos: "))
monto = float(input("Ingrese monto total de la compra: $"))
medio = input("Medio de pago (efectivo, debito, credito, mercado_pago): ").lower()

descuento = 0
recargo = 0

if medio == "efectivo":
    descuento = monto * 0.15
elif medio == "debito":
    descuento = monto * 0.10
elif medio == "credito":
    recargo = monto * 0.05
elif medio == "mercado_pago":
    if monto > 10000:
        descuento = monto * 0.20

monto_final = monto - descuento + recargo

if cantidad > 10:
    monto_final *= 0.95  # descuento extra del 5%

print(f"\nCliente: {cliente}")
print(f"Productos: {cantidad}")
print(f"Monto inicial: ${monto:,.2f}".replace(",", "."))
print(f"Descuentos aplicados: ${descuento:,.2f}".replace(",", "."))
print(f"Recargos aplicados: ${recargo:,.2f}".replace(",", "."))
print(f"Total a pagar: ${monto_final:,.2f}".replace(",", "."))
