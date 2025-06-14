#Crea una funcion recursiva en Python que reciba un numero entero en base decimal y devuelva su representacion en BINARIO
#como una cadena de texto.

#Funcion

def decimal_a_binario (num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_a_binario(num//2)+ str(num%2)
    
#algoritmo

numero=int(input("Ingrese un numero entero positivo: "))
if numero >= 0:
    binario= decimal_a_binario(numero)
    print(f"El numero {numero} en binario es: {binario}")
else:
    print("Por favoir ingresa un numero entero positivo")