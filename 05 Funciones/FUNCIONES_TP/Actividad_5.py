def segundos_a_horas(segundos):
    horas = segundos / 3600
    return f"{horas:.2f}"   # Con esta funcion logro que al momento de darme la hora, solo imprima dos decimales. Es valido el "return horas". pero me va a imprimir varios decimales

#programa Principal

segundos = int(input("Ingrese los segundos que quiera convertir a hora: "))
print(f"{segundos_a_horas(segundos)} hs")