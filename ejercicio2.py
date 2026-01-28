def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print(" Error: Debe ingresar un número entero.")

def leer_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print(" Error: El valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print(" Error: Debe ingresar un número válido.")

def leer_texto(mensaje):
    while True:
        texto = input(mensaje)
        if texto.replace(" ", "").isalpha():
            return texto
        else:
            print(" Error: Solo se permiten letras.")

def leer_tipo_vendedor():
    while True:
        tipo = leer_entero(
            "Tipo de vendedor (1: Puerta a puerta, 2: Telemercadeo, 3: Ejecutivo): "
        )
        if tipo in (1, 2, 3):
            return tipo
        else:
            print(" Error: Tipo de vendedor inválido.")

def calcular_comision(tipo_vendedor, ventas):
    if tipo_vendedor == 1:
        return ventas * 0.20
    elif tipo_vendedor == 2:
        return ventas * 0.15
    elif tipo_vendedor == 3:
        return ventas * 0.25

def procesar_vendedor():
    nombre = leer_texto("Nombre: ")
    tipo = leer_tipo_vendedor()
    ventas = leer_flotante("Valor de ventas del mes: ")

    comision = calcular_comision(tipo, ventas)

    print("\n--- Resumen del vendedor ---")
    print(f"Nombre: {nombre}")
    print(f"Ventas del mes: ${ventas:.2f}")
    print(f"Comisión a pagar: ${comision:.2f}")
    print("----------------------------\n")

    return ventas, comision

def leer_vendedores():
    total_ventas = 0
    total_comisiones = 0

    print("Ingrese los datos de los vendedores")
    print("La lista termina cuando la cédula sea -1\n")

    cedula = leer_entero("Cédula: ")
    while cedula != -1:
        ventas, comision = procesar_vendedor()

        total_ventas += ventas
        total_comisiones += comision

        cedula = leer_entero("Cédula: ")

    return total_ventas, total_comisiones

def mostrar_resultados(total_ventas, total_comisiones):
    print("\n===== RESUMEN GENERAL =====")
    print(f"Total ventas del mes: ${total_ventas:.2f}")
    print(f"Total a pagar por comisiones: ${total_comisiones:.2f}")
    print("===========================")

def main():
    total_ventas, total_comisiones = leer_vendedores()
    mostrar_resultados(total_ventas, total_comisiones)

main()