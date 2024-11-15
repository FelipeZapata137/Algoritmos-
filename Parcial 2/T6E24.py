capital=float(input("Introduce la cantidad a invertir: "))
interesAnual=float(input("Introduce el interés anual en porcentaje (por ejemplo, 5 para 5%): "))
numeroAños=int(input("Introduce el número de años de la inversión: "))

interes_decimal=interesAnual/100

for año in range(1,(numeroAños+1)):
    cantidad_invertida=capital*(1 + interes_decimal) ** año
    print("Año",año,":",round(cantidad_invertida, 2))