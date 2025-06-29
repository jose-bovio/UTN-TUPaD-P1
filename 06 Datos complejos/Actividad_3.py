precio_frutas={"banana":1200,"anana":2500,"melon":3000,"uva":1450}

precio_frutas["naranja"]= 1200
precio_frutas["manzana"]= 1500
precio_frutas["pera"]= 2300

#Precios Actualizados

precio_frutas["banana"]= 1330
precio_frutas["manzana"]= 1700
precio_frutas["melon"]= 2800

#Lista de frutas disponibles sin su precio

lista_frutas = list(precio_frutas.keys())   # .keys() de un diccionario devuelve una vista de todas las claves del diccionario.

print(lista_frutas)