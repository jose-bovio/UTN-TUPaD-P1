#Agenda con eventos

agenda ={("Lunes","10:00"):"Reunion de equipo",("Martes","14:30"):"Clase de programacion 1",("Miercoles","17:00"):"Grupo de Matematicas",("jueves","16:00"):"Clase OE",("Viernes","09:00"):"clase AYSO"}

# Consultar día y horario

dia = input("Ingresa el día que querés consultar: ").capitalize()
hora = input("Ingresa la hora (Formato HH:MM): ")

clave = (dia, hora)

# Verificar si hay un evento en esa fecha y hora

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese horario.")