def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return promedio
#Programa Princiapal

num1 = float(input("Ingrese un numero para a : "))
num2 = float(input("Ingrese un numero para b: "))
num3 = float(input("Ingrese un numero para c: "))

print(f"el promedio de los tres numeros ingresados es: {calcular_promedio(num1,num2,num3)}")