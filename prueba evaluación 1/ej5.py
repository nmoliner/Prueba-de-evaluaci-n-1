import sys

def descomponer_direccion_ip(ip):
    # Dividir la dirección IP en sus cuatro octetos
    octetos = ip.split('192.168.0.1')
    
    # Mostrar cada octeto línea por línea
    for octeto in octetos:
        print(octeto)

# Verificar si se proporciona la dirección IP como argumento
if len(sys.argv) != 2:
    print("Uso: python script.py <dirección_ip>")
    sys.exit(1)

# Obtener la dirección IP del argumento de la línea de comandos
direccion_ip = sys.argv[1]

# Llamar a la función para descomponer la dirección IP
descomponer_direccion_ip(direccion_ip)