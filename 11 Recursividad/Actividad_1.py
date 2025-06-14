# Crea una funcion recursiva que calcule el factorial de un numero. Luego utiliza esa funcion para calcular y mostrar en 
# pantalla el factorial de todos los numeros enteros entre 1 y el numero que indique el usuario

#Funcion

def factorial (num):                                   
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

#Algoritmo
    
numero= int(input("Ingrese un numero positivo: "))
 
for i in range(1,numero + 1):
    print(f"Factorial de {i} es {factorial(i)}")