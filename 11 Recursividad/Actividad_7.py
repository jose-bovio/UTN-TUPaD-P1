#Un niño esta construyendo una piramide con bloques. En el nivel mas bajo coloca n bloques, en el siguiente nivel uno menos(n-1),
# y asi sucesivamente hasta llegar al ultimo nivel con solo  un bloque. Escribi una funcion recursiva contar_bloque(n) que reciba el numero 
# de bloques en el nivel mas bajo y devuelva el total de loquers que necesita para construir toda la piramide.
 
#Funcion

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)
    
#Algoritmo

num=int(input("Ingrese el numero de bloques que hay que en el nivel mas bajo: "))

if num >= 1:
    total = contar_bloques(num) 
    print(f"se necesitan {total} bloques para construir la piramide")
else:
    print("ERROR !!! Ingrese un numero entero mayor o igual a 1")

