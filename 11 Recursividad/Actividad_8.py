# Escribi una funcion recursiva llamada contar_digito(numero,digito= que reciba un numero entero positivo(numero) y un digito entre(0 y 9) y devuelva cuantas 
# veces aparece ese digito dentro del numero

#Funcion

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero //10,digito)
    else:
        return contar_digito(numero//10,digito)
    
#Algoritmo

num=int(input("ingrese un numero entero, positivo: "))
dig=int(input("Ingrese un digito del 0 a 9: "))

if 0 <= dig <= 9 and num >=0:
    resultado= contar_digito(num,dig)
    print(f"El digito {dig}, aparece {resultado} veces en el numero {num}")
else:
    print("El numero no es positivo o el digito ingresado no esta entre 0 y 9")