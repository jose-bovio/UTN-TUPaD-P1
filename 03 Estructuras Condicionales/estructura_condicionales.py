#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

Edad = int(input("Ingrese su edad"))

if Edad >= 18:
    print("Es Mayor de edad")
else:
    print("No es mayor de edad")    

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

Nota = int(input("Ingrese una Nota de 1 a 10 "))

if Nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")    

    # Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

Numero = int(input("Ingrese un numero Par"))

if Numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un numero par")     

    #Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

Edad = int(input("Ingrese su edad"))

if Edad < 12:
    print("Usted es un niño/a")
elif Edad >= 12 and Edad < 18:
    print("Usted es adolecente")
elif Edad >= 18 and Edad < 30:
    print("Usted es adulto/a, joven")
elif Edad >= 30:
    print("Usted es adulto")        

 # Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

Contraseña = input("Ingrese una contraseña")

if 8 <= len(Contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingres una contraseña que contenga entre 8 y 14 caracteres")

 # escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Si a import le agregamos la sentensia "AS" nos permite agregar un alias a statistics
import statistics as st 

import random
numeros_aleatorios  = [random.randint(1, 100) for i in range(50)]

#Calculamos el promedio de los numeros aleatorios
print(st.mean(numeros_aleatorios))

# Calculamos la media de los numeros aleatorios
print(st.median(numeros_aleatorios))

# Calculamos el numero que mas se repite en el rango elegido aleatoriamente
print(st.mode(numeros_aleatorios))

#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla

Palabra = input("Ingrese una frase o palabra")

#El índice -1 se usa para acceder al último carácter de la cadena. En Python, los índices negativos cuentan desde el final de la cadena, donde -1 representa el último carácter
#La función .lower() convierte el carácter (o toda la cadena) a minúsculas.En este caso, se usa para asegurarse de que el último carácter se compare en minúsculas,
#  sin importar si originalmente estaba en mayúsculas o no.
#ultimo_caracter = texto[-1].lower() toma el último carácter de la cadena texto, lo convierte a minúsculas (si no lo está ya) y lo almacena en la variable ultimo_caracter

ultimo_caracter = Palabra [-1].lower()

if ultimo_caracter in 'aeiou':
   Palabra += "!"
print(f"La frase o palabra ingresada es {Palabra}")

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

Nombre = input("Ingrese su nombre")
print("seleccione la opcion en la que quiera imprimir su nombre")
print("1.Mayusculas")
print("2.Minusculas")
print("3. Primer letra mayuscula")

opcion = int(input("ingrese el numero de la opcion deseada"))

if opcion == 1:
    resultado = Nombre.upper()
elif opcion == 2:
    resultado = Nombre.lower()
elif opcion == 3:
    resultado = Nombre.title()

print("Su nombre segun la opcion elegida es: ", resultado)

#ACTIVIDAD NUMERO 9

terremoto = float(input("Ingrese la magnitud del terremoto"))

if terremoto < 3:
    magnitud = "muy leve"
elif terremoto >= 3 and terremoto < 4:
    magnitud = "Leve"
elif terremoto >= 4 and terremoto < 5:
    magnitud = "Moderado"
elif terremoto >= 5 and terremoto < 6:
    magnitud = "Fuerte"
elif terremoto >= 6 and terremoto < 7:
    magnitud = " Muy Fuerte"
elif terremoto >= 7:
    magnitud = "Extremo" 

print("La magnitud del terremoto es: ", magnitud)    

#ACTIVIDAD NUMERO 10
hemisferio = input("Ingrese en qué hemisferio se encuentra (NORTE/SUR): ").capitalize()
mes = int(input("Ingrese en qué mes del año se encuentra (de 1 al 12): "))
dia = int(input("Ingrese qué día es: "))


def estacion_seleccionada(hemisferio, mes, dia):
    
    if hemisferio == "Norte":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and not (mes == 3 and dia > 20)):
            return "Invierno"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and not (mes == 6 and dia > 20)):
            return "Primavera"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and not (mes == 9 and dia > 20)):
            return "Verano"
        else:
            return "Otoño"
    
    
    elif hemisferio == "Sur":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and not (mes == 3 and dia > 20)):
            return "Verano"
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and not (mes == 6 and dia > 20)):
            return "Otoño"
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and not (mes == 9 and dia > 20)):
            return "Invierno"
        else:
            return "Primavera"


estacion = estacion_seleccionada(hemisferio, mes, dia)

print(f"La estación en el hemisferio {hemisferio} es: {estacion}")