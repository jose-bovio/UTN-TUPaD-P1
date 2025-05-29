def tabla_de_multiplicar(numero):
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Programa principal
numero = int(input("Ingrese un número: "))
tabla_de_multiplicar(numero)