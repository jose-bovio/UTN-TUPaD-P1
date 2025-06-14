# Crea una funcion recursiva que calcule el valor de la serie de Fibonacci en la posicion indicada. 
# Posteriormente, muestre la serie completa hasta la posicion que el usuario especifique.

#Funcion

def fibo_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibo_recursivo(posicion-1)+fibo_recursivo(posicion-2)
    
#Algoritmo    
    
ubicacion = int(input("Ingresa la posicion de fibonacci que quieras ver: "))

print("SERIE DE FIBONACCI")

for i in range(ubicacion+1):
    print(f"Fibonacci({i} = {fibo_recursivo(i)})")