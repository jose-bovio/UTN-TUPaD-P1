contactos={"juan":"254321","pedro":"741852","lorena":"001320"}

while True:
    nombre = input("ingrese el nombre del contacto o salir para terminar").lower()
    if nombre == "salir":
        print("Programa terminado")
    elif nombre in contactos:
        print(f"numero de {nombre}: {contactos[nombre]}")
    else:
        print("El contacto no esta en la agenda")