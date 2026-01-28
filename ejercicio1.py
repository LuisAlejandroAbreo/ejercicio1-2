def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))

            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
            elif maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
            else:
                return valor

        except ValueError:
            print("Error: debe ingresar un número entero.")

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto.isalpha():
            return texto
        else:
            print("Error: solo se permiten letras.")

def mostrar_programas():
    print("\nProgramas académicos:")
    print("1. Técnico en Sistemas")
    print("2. Técnico en Desarrollo de Videojuegos")
    print("3. Técnico en Animación Digital")

def mostrar_becas():
    print("\nTipos de beca:")
    print("1. Beca por rendimiento académico (50%)")
    print("2. Beca cultural/deportes (40%)")
    print("3. Sin beca")

def obtener_valor_matricula(programa):
    if programa == 1:
        return 800000
    elif programa == 2:
        return 1000000
    elif programa == 3:
        return 1200000

def calcular_descuento(valor_matricula, beca):
    if beca == 1:
        return valor_matricula * 0.50
    elif beca == 2:
        return valor_matricula * 0.40
    else:
        return 0

def liquidar_matricula():
    print("\n=== LIQUIDACIÓN DE MATRÍCULA ===")

    codigo = leer_entero("Ingrese el código del estudiante: ")
    nombre = leer_texto("Ingrese el nombre del estudiante: ")

    mostrar_programas()
    programa = leer_entero("Seleccione el programa: ", 1, 3)

    mostrar_becas()
    beca = leer_entero("Seleccione el tipo de beca: ", 1, 3)

    valor_matricula = obtener_valor_matricula(programa)
    descuento = calcular_descuento(valor_matricula, beca)
    valor_pagar = valor_matricula - descuento

    print("\n--- RESULTADO ---")
    print("Código:", codigo)
    print("Nombre:", nombre)
    print("Valor matrícula:", valor_matricula)
    print("Descuento:", descuento)
    print("Valor a pagar:", valor_pagar)

def main():
    opcion = 0

    while opcion != 2:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Liquidar matrícula")
        print("2. Salir")

        opcion = leer_entero("Seleccione una opción: ", 1, 2)

        if opcion == 1:
            liquidar_matricula()
        else:
            print("Programa finalizado. ¡Hasta luego!")

main()