def saludar_usuario(nombre):
    saludo = "HOLA,"+ nombre + "!!!"
    return saludo

#Programa Principal

nombre=input("Ingrese su nombre")
print(saludar_usuario(nombre))
