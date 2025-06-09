import time
import matplotlib.pyplot as plt
import cProfile  # Importa el módulo cProfile
import pstats    # Módulo para procesar y presentar los resultados de cProfile

# Algoritmo 1: Buscar pares usando if dentro de un bucle
def pares_con_if(n):
    pares = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            pares.append(i)
    return pares

# Algoritmo 2: Usar range con paso de 2
def pares_con_range(n):
    return list(range(2, n + 1, 2))

# Función para medir el tiempo de ejecución (la mantendremos para referencia)
def medir_tiempo(funcion, n):
    inicio = time.time()
    funcion(n)
    fin = time.time()
    return fin - inicio

# Esta función encapsulará las llamadas a los algoritmos que queremos perfilar.
# cProfile.run() necesita una cadena de texto para ejecutar.
def ejecutar_algoritmos_para_cpu_profile(n_valor):
    print(f"\n--- Ejecutando pares_con_if para cProfile con n = {n_valor:,} ---")
    _ = pares_con_if(n_valor) # Asignamos a _ porque no necesitamos el retorno para el perfilado

    print(f"\n--- Ejecutando pares_con_range para cProfile con n = {n_valor:,} ---")
    _ = pares_con_range(n_valor)


# Programa principal
if __name__ == "__main__":
    # --- Parte 1: Análisis de CPU con cProfile ---
    print("--- Iniciando Análisis de CPU con cProfile ---")
    print("Esto te mostrará dónde tu programa gasta más tiempo de procesamiento.")

    # Elegimos un valor de 'n' para el perfilado de CPU.
    # Un valor muy grande (ej. 10^7) puede hacer el perfilado muy lento.
    # 10^6 suele ser un buen balance.
    n_para_perfilado_cpu = 10**6 

    # Guardamos los resultados del perfilado en un archivo. Esto es lo más práctico
    # para analizarlo después con 'pstats' o herramientas de visualización.
    output_filename = "cpu_profile_results.prof"
    print(f"\nEjecutando cProfile para n = {n_para_perfilado_cpu:,} y guardando resultados en '{output_filename}'...")
    
    # cProfile.run() toma una cadena de código a ejecutar y un nombre de archivo para guardar el perfil.
    cProfile.run(f'ejecutar_algoritmos_para_cpu_profile({n_para_perfilado_cpu})', output_filename)

    print("\n--- Resultados del perfilado de CPU (top 10 funciones por tiempo acumulado) ---")
    # Usamos pstats para cargar y analizar los resultados del archivo .prof
    stats = pstats.Stats(output_filename)
    stats.sort_stats("cumtime") # Ordenamos los resultados por 'tiempo acumulado' (cumtime)
    stats.print_stats(10)       # Imprimimos las 10 funciones que más tiempo acumularon

    print(f"\nPara un análisis más detallado o visual, puedes usar 'snakeviz':")
    print(f"Instala con: pip install snakeviz")
    print(f"Ejecuta con: snakeviz {output_filename}")


    # --- Parte 2: Medición de Tiempos y Generación de Gráficos 
    print("\n--- Iniciando Medición de Tiempos para el Gráfico (puede tardar para n grandes) ---")
    valores_n_para_grafico = [10**i for i in range(1, 8)] # Valores originales para el grafico de tiempo
    tiempos_if = []
    tiempos_range = []

    for n in valores_n_para_grafico:
        print(f"\nProbando con n = {n:,}")
        
        tiempo_if = medir_tiempo(pares_con_if, n)
        tiempos_if.append(tiempo_if)
        print(f"[Con if] Tiempo: {tiempo_if:.6f} segundos")
        
        tiempo_range = medir_tiempo(pares_con_range, n)
        tiempos_range.append(tiempo_range)
        print(f"[Con range paso 2] Tiempo: {tiempo_range:.6f} segundos")

    #genracion de Grafico de Tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n_para_grafico, tiempos_if, label='pares_con_if (Bucle con If)', marker='o')
    plt.plot(valores_n_para_grafico, tiempos_range, label='pares_con_range (Range con Paso)', marker='x')
    plt.xscale('log')
    plt.xlabel('Valor de n (escala logarítmica)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparación de Eficiencia Temporal de Algoritmos para Números Pares')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()