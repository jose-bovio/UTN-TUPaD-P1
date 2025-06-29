#Estudiantes y aprobaciones de parciales

parcial1={"juan","pedro","maria","ana"}
parcial2={"juan","maria","sofia","luz"}

#Alumnos que aprobaron ambos parciales

ambos = parcial1 & parcial2
print("Alumnos que aprobaron ambos parciales:", ambos)

#Alumnos que solo aprobaron uno de los dos parciales

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos parciales:", solo_uno)


#Alumnos que aprobaron al menos un parcial

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)