frase = input("ingresa una frase: ")

palabras= frase.lower().split()   # .split() Divide una cadena de texto en partes, separándola por espacios (por defecto). Devuelve una lista de palabras.

palabras_unicas= set(palabras)
print("Palabras unicas")
print(palabras_unicas)

frecuencia={}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] +=1
    else:
        frecuencia[palabra]=1

print("la frecuncia de cada palabra es: ")
print(frecuencia)