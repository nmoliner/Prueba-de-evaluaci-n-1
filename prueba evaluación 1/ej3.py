def encontrar_palabras_comunes(lista1, lista2):
    # Convertir las listas en conjuntos para eliminar duplicados
    set1 = set(lista1)
    set2 = set(lista2)
    
    # Encontrar la intersección de los conjuntos
    palabras_comunes = set1.intersection(set2)
    
    # Convertir el conjunto en una lista
    lista_comunes = list(palabras_comunes)
    
    return lista_comunes

