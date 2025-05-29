def informacion_personal(nombre,apellido,edad,residencia):
    informacion = "Soy " + nombre + apellido + " , tengo " + edad + " y vivo " + residencia
    return informacion

#Programa Primaria
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("ingrese su edad: ")
residecia = input("Ingrese su lugar de residencia: ")
print(informacion_personal(nombre,apellido,edad,residecia))