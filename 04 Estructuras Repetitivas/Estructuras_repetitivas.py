#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for contador in range(0,101):
    print(contador)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un numero"))

digitos = 0

while numero > 0:
    numero = numero // 10
    digitos += 1
print(f"El numero tiene {digitos} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num_A = int (input("Ingrese un numero"))
num_B = int (input("ingrese un numero"))

suma = 0
for i in range(num_A +1,num_B):
    suma += i

print(f"La suma entre {num_A} y {num_B} es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume ensecuencia.
#  El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma_total = 0
numero = 1

print("Ingresá números enteros. Ingresá 0 para finalizar.")


while numero != 0:
    numero = int(input("Ingresá un número: "))
    if numero != 0:
        suma_total += numero

print("La suma total es:", suma_total)

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número

x = 7
Numero = int(input("Ingrese un numero X del  0 a 9: "))

while Numero != x:
    print("Incorrecto. Intentá de nuevo.")
    Numero = int(input("Adiviná el número: "))

print(f"Correcto el numero X es: {x} ")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("A continuacion vamos a imprimir todos los numeros pares de 0 a 100. Comencemos !!!!")
Contador = 0
while Contador < 100:
        Contador = Contador + 2
        print(Contador)
print("Nuestro conteo a finalizado !!!!")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

Num_a = int(input("Ingrese un numero entero: "))
Num_b = 0
suma = 0
for i in range (Num_b,Num_a):
    suma = suma + i
print(f"La suma total de todos los numeros es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el  programa debe indicar cuántos de estos números son pares,
#  cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar
#  preparado para procesar 100 números con un solo cambio).

numeros = 12
par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(1,numeros + 1):
    numero = int(input("Ingrese los numeros: "))
     
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1

    
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    

print("El total de numeros pares es :", par)
print("El total de numeros impares es:", impar)
print("Cantidad de números positivos:", positivo)
print("Cantidad de números negativos:", negativo)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

numeros = 5
sumatoria = 0

for numeros in range (1,numeros+1):
    print("Ingrese sus numeros: ", numeros)
    numeros= float(input())
    sumatoria = sumatoria + numeros

print("La suma de todos los numeros es: ",sumatoria)
print("El valor promedio es: ",(sumatoria / numeros))

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("ingrese un numero: ")

invertir_numero = numero[::-1]

print("Su numero invertido es: ", invertir_numero)

