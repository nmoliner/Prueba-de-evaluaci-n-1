import re

def formatear_receta(cadena):
    # Voltear la cadena
    cadena_volteada = cadena[::-1]

    # Extraer el nombre de la receta y el número de calorías
    match = re.search(r'(\d+)(.*)(\d+)', cadena_volteada)
    if match:
        calorías = match.group(1)
        nombre_receta = match.group(2).strip()

        # Formatear la cadena de salida
        salida = f"La receta de {nombre_receta} contiene {calorías} calorías."
        return salida

    return "No se pudo extraer la información de la receta."

# Prueba
cadena = "321 saícodelac 123"
print(formatear_receta(cadena))