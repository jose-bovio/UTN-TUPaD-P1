def celsius_a_fahrenheit(celsius) :
    F= (celsius*1.8) + 32
    return F
#Programa principal

Gc = float(input("ingrese los grados celsius: "))
print(celsius_a_fahrenheit(Gc),"º Fahrenheit")
