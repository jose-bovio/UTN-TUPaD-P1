# Crea una funcion recursiva que calcule la potencia de un numero base elevado a un exponente utilizando la formula ... 
# Prueba esta funcion en un algoritmo general

#Funcion

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

#Algoritmo

base= int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponenete (numero entero): "))

resultado= potencia(base,exponente)
print(f"{base}^{exponente} = {resultado}")