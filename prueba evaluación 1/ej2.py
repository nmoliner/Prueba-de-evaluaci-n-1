capital_inicial = 1000
tasa_interes = float(input("Ingrese la tasa de interés anual (entre 1% y 10%): "))
num_anios = int(input("Ingrese el número de años: "))

if tasa_interes < 1 or tasa_interes > 10:
    print("La tasa de interés debe estar entre 1% y 10%.")
else:
    tasa_interes_decimal = tasa_interes / 100
    capital_final = capital_inicial * (1 + tasa_interes_decimal) ** num_anios
    print("El capital final es:", capital_final)