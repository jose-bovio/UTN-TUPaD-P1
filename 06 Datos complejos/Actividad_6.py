alumnos={"juan":(7,8.5,6),"manuel":(9,7.5,7),"sofia":(3,9,7)}

for alumno, notas in alumnos.items():
    promedio = sum(notas)/3
    print(f"{alumno}:promedio={promedio:2f}")