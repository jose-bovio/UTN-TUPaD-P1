def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return f"{imc:.2f}"

#Programa principal

peso = float(input("Ingrese su peso (KG): "))
altura = float(input("Ingrese su altura (m): "))
print("Su IMC ES: " + calcular_imc(peso,altura))
