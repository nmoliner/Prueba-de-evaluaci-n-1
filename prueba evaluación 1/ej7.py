def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    else:
        inventario.append(item)

# Ejemplo de inventario inicial
inventario = ["espada", "poción", "escudo"]

# Nuevo ítem a añadir
nuevo_item = "amuleto"

try:
    agregar_item(inventario, nuevo_item)
    print("Ítem agregado exitosamente al inventario.")
except ValueError as e:
    print(f"Error: {e}")

print("Inventario actualizado:", inventario)

