import time

# Algoritmo 1: Buscar pares usando if dentro de un bucle

def pares_con_if(n):              #  Declara una función llamada pares_con_if que toma un parámetro n (el número máximo hasta donde se buscarán pares).
    pares = []                    #Se crea una lista vacía llamada pares que almacenará los números pares encontrados.
    for i in range(1, n + 1):     #Bucle que recorre desde 1 hasta n (inclusive). Se usa n + 1 porque range excluye el valor superior.
        if i % 2 == 0:            #Condición que verifica si el número i es par (el residuo de dividir por 2 debe ser cero).
            pares.append(i)       #Si la condición se cumple, se añade i a la lista pares.
    return pares                  #Devuelve la lista completa de números pares encontrados.

# Algoritmo 2: Usar range con paso de 2

def pares_con_range(n):                   #Declara una función llamada pares_con_range que también toma n como parámetro.
    return list(range(2, n + 1, 2))       #Genera una secuencia que comienza en 2, termina en n (inclusive), 
                                        #avanzando de 2 en 2 (por eso solo incluye pares).list(...)
                                        #Convierte esa secuencia en una lista.


# Función para medir el tiempo de ejecución

def medir_tiempo(funcion, n):             #Define una función que toma como entrada otra función (funcion) y un valor n.
    inicio = time.time()                  #Guarda el tiempo actual justo antes de ejecutar la función.
    funcion(n)                            #Ejecuta la función recibida como argumento con el parámetro n.
    fin = time.time()                     #Guarda el tiempo justo después de que la función terminó de ejecutarse.
    return fin - inicio                   #Calcula y devuelve el tiempo transcurrido en segundos

# Programa principal

if __name__ == "__main__":        #   Esta línea asegura que el bloque de código debajo solo se ejecutará si el archivo se ejecuta directamente 
                                    #(no si es importado como módulo en otro script).
    
    # Valores de n que vamos a probar (desde 10^0 hasta 10^7 en escala logarítmica)
    
    valores_n = [10**i for i in range(1, 8)]                        #Crea una lista con potencias de 10: [10^1, 10^2, ..., 10^7] → [10, 100, 1000, ..., 10,000,000]
    tiempos_if = []                                                   #Inicializa dos listas vacías para guardar los tiempos que tomarán ambos algoritmos.
    tiempos_range = []                                                    #                                 "

    print("Comparando tiempos de ejecución...")                         #Muestra un mensaje para indicar el inicio de la comparación.
    for n in valores_n:                                                    #Itera sobre los valores de n, imprimiendo cada uno con separadores de miles.
        print(f"\nProbando con n = {n:,}")                                         #                             "
        
        tiempo_if = medir_tiempo(pares_con_if, n)                                          #Mide el tiempo que tarda pares_con_if(n).
        tiempos_if.append(tiempo_if)                                                       #Guarda ese tiempo en la lista tiempos_if.
        print(f"[Con if] Tiempo: {tiempo_if:.6f} segundos")                                #Imprime el tiempo en formato con 6 decimales.
        
        tiempo_range = medir_tiempo(pares_con_range, n)                                    #Mide el tiempo que tarda pares_con_range(n).
        tiempos_range.append(tiempo_range)                                                 #Guarda ese tiempo en tiempos_range.
        print(f"[Con range paso 2] Tiempo: {tiempo_range:.6f} segundos")                   #Imprime el tiempo de ejecución correspondiente.
