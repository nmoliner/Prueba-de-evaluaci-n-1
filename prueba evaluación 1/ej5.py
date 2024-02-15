
import sys

def descomponer_direccion_ip(ip):
    # Dividir la dirección IP en sus cuatro octetos
    octetos = ip.split('.')
    
    # Mostrar cada octeto línea por línea
    for octeto in octetos:
        print(octeto)

def validar_direccion_ip(ip):
    # Dividir la dirección IP en sus cuatro octetos
    octetos = ip.split('.')
    
    # Verificar si la dirección IP tiene cuatro octetos
    if len(octetos) != 4:
        return False
    
    # Verificar si cada octeto es un número entero válido
    for octeto in octetos:
        try:
            octeto_int = int(octeto)
            if octeto_int < 0 or octeto_int > 255:
                return False
        except ValueError:
            return False
    
    # La dirección IP es válida
    return True

# Pedir al usuario que introduzca la dirección IP
direccion_ip = input("Introduce la dirección IP: ")

# Verificar si la dirección IP es válida
if not validar_direccion_ip(direccion_ip):
    print("La dirección IP introducida no es válida")
    sys.exit(1)

# Llamar a la función para descomponer la dirección IP
descomponer_direccion_ip(direccion_ip)