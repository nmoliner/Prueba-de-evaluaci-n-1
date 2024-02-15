from queue import PriorityQueue

# Crear una cola prioritaria
cola_misiones = PriorityQueue()

# Agregar misiones con sus niveles de dificultad
cola_misiones.put((3, "Misión final"))  # Ejemplo de misión final con dificultad 3
cola_misiones.put((1, "Misión secundaria 1"))  # Ejemplo de misión secundaria con dificultad 1
cola_misiones.put((2, "Misión secundaria 2"))  # Ejemplo de misión secundaria con dificultad 2

# Mostrar las misiones en orden de dificultad
print("Misiones:")
while not cola_misiones.empty():
    _, mision = cola_misiones.get()
    print(mision)
