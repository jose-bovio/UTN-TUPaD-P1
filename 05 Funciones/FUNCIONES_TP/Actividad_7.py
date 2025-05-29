def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    return (suma, resta, multiplicacion, division)

# Programa Principal
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

resultado = operaciones_basicas(a, b)

print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")