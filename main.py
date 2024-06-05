from Constante import get_element_at_index

# Importamos el paquete time para medir el tiempo de ejecución
import time

# Registramos el tiempo inicial antes de la búsqueda binaria
start_time = time.time()

print("constante: ", get_element_at_index([10, 20, 30, 40, 50], 2))  # Salida: 30

# Registramos el tiempo final después de las búsquedas binarias
end_time = time.time()

# Calculamos el tiempo de ejecución para las búsquedas binarias
execution_time = end_time - start_time

# Imprimimos el tiempo de ejecución de las búsquedas binaria

print("Tiempo de ejecución: {:.5f} segundos".format(execution_time))
