def palabras_comunes(lista1, lista2):
    # Convertir las listas a conjuntos para eliminar duplicados
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Encontrar la intersección de los conjuntos
    palabras_repetidas = set1.intersection(set2)
    
    # Convertir el resultado de nuevo a una lista
    palabras_repetidas_lista = list(palabras_repetidas)
    
    return palabras_repetidas_lista

# Ejemplo de listas de palabras
lista1 = ["hola", "mundo", "python", "hola"]
lista2 = ["python", "mundo", "programación", "java"]

# Encontrar las palabras comunes
palabras_comunes_lista = palabras_comunes(lista1, lista2)

# Mostrar el resultado
print("Palabras comunes en ambas listas:")
print(palabras_comunes_lista)
