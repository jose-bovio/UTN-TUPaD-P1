import time
import matplotlib.pyplot as plt
from memory_profiler import profile # Importa el decorador profile

# Algoritmo 1: Buscar pares usando if dentro de un bucle
@profile # Decorador para perfilar el uso de memoria de esta función
def pares_con_if(n):
    pares = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares.append(i)
    return pares

# Algoritmo 2: Usar range con paso de 2
@profile # Decorador para perfilar el uso de memoria de esta función
def pares_con_range(n):
    return list(range(2, n + 1, 2))

# Función para medir el tiempo de ejecución (no se modifica para memory_profiler)
def medir_tiempo(funcion, n):
    inicio = time.time()
    funcion(n)
    fin = time.time()
    return fin - inicio

# Programa principal
if __name__ == "__main__":
    # Valores de n que vamos a probar para el análisis de memoria.
    # Se recomienda usar valores más pequeños para memoria inicialmente (ej. hasta 10^6).
    # Para n=10^7, la salida de memory_profiler puede ser muy extensa y lenta.
    valores_n_para_memoria = [10**4, 10**5, 10**6] # Valores de n para análisis de memoria
    
    print("Iniciando análisis de memoria con memory_profiler...")
    print("Para ver los resultados detallados por línea, ejecuta este script con:")
    print(">>> python -m memory_profiler tu_archivo.py\n")

    for n in valores_n_para_memoria:
        print(f"\n--- Analizando memoria para n = {n:,} ---")
        
        print("\n--- Ejecutando pares_con_if (análisis de memoria) ---")
        # Llamamos a la función para que memory_profiler la analice.
        # Asignamos el resultado a '_' para indicar que no lo usaremos más.
        _ = pares_con_if(n) 
        
        print("\n--- Ejecutando pares_con_range (análisis de memoria) ---")
        # Hacemos lo mismo para la segunda función.
        _ = pares_con_range(n) 
        
        # Opcional: Puedes mantener la medición de tiempos aquí si quieres ambos resultados
        # en una sola ejecución, pero ten en cuenta que `memory_profiler` añade una
        # pequeña sobrecarga. Para mediciones de tiempo muy precisas, es mejor usar
        # `timeit` por separado.
        print("\n--- Midiendo tiempos de ejecución (no afectado por @profile) ---")
        tiempo_if = medir_tiempo(pares_con_if, n)
        print(f"[Con if] Tiempo: {tiempo_if:.6f} segundos")
        
        tiempo_range = medir_tiempo(pares_con_range, n)
        print(f"[Con range paso 2] Tiempo: {tiempo_range:.6f} segundos")
