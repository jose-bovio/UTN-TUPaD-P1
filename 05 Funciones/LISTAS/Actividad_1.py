#Crear una lista con los numeros del 1 al 100 que sean multiplos de 4. utilizar la funcion range.

Lista = list(range(0,101,4))
print(Lista)

#otra opcion 

for i in range(0,101):
    if i % 4 == 0:
        print(i)

