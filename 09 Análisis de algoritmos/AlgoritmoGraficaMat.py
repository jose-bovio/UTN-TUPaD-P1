import time
import matplotlib.pyplot as plt

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

# Función para medir el tiempo de ejecución
def medir_tiempo(funcion, n):
    inicio = time.time()
    funcion(n)
    fin = time.time()
    return fin - inicio

# Programa principal
if __name__ == "__main__":
    # Valores de n que vamos a probar (desde 10^1 hasta 10^7 en escala logarítmica)
    valores_n = [10**i for i in range(1, 8)]
    tiempos_if = []
    tiempos_range = []

    print("Comparando tiempos de ejecución...")
    for n in valores_n:
        print(f"\nProbando con n = {n:,}")
        
        tiempo_if = medir_tiempo(pares_con_if, n)
        tiempos_if.append(tiempo_if)
        print(f"[Con if] Tiempo: {tiempo_if:.6f} segundos")
        
        tiempo_range = medir_tiempo(pares_con_range, n)
        tiempos_range.append(tiempo_range)
        print(f"[Con range paso 2] Tiempo: {tiempo_range:.6f} segundos")

    # Crear la gráfica con el formato solicitado
    plt.figure(figsize=(10, 6))
    plt.plot(valores_n, tiempos_if, label='pares_con_if (Bucle con If)', marker='o')
    plt.plot(valores_n, tiempos_range, label='pares_con_range (Range con Paso)', marker='x')
    plt.xscale('log')
    plt.xlabel('Valor de n (escala logarítmica)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Comparación de Eficiencia Temporal de Algoritmos para Números Pares')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()