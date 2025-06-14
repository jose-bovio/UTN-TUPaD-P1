# Escribi una funcion recursiva en Python llamada suma:digitos(n) que reciba un numero entero positivo
# y devuelva la suma de todo sus digitos.

#Funcion

def suma_digitos(num):
    if num < 10:
        return num
    else:
        return(num % 10) + suma_digitos (num // 10)

#Algoritmo

numero = int(input("Ingrese un numero entero positivo: "))

if numero >= 0:
    resultado= suma_digitos(numero)
    print(f"El numero ingresado fue el {numero} y la suma de sus digitos es: {resultado} ")
else:
    print("ingrese un numero entero positivo")
