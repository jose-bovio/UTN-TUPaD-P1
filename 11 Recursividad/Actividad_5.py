# Implementa una funcion recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacio ni tildes, y devuelva True si es un 
# palindromo o Flase si no lo es.

#Funcion

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#Algoritmo

palabra = input(" Ingrese una palabra (sin espacios): ")

if es_palindromo(palabra):
    print(f"{palabra} es un palindromo.")
else:
    print(f"{palabra} no es una palindromo. ")