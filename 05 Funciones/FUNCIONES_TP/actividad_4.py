def calcular_area_circulo(radio):
    area = 3.1415 * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1415 * radio
    return perimetro

#Programa Principal

radio = float(input("Ingrese el radio: "))
print("Área del círculo:", calcular_area_circulo(radio))
print("Perímetro del círculo:", calcular_perimetro_circulo(radio))
