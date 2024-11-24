sumaTotal = 0
sumaDigitosTotal = 0

print("Ingresa un número. Para terminar, ingresa 0.")

while True:
    numero = int(input("Ingresa un número: "))

    if numero == 0:
        break
    
    suma_digitos = sum(int(digito) for digito in str(abs(numero)))
    print("La suma de los dígitos de",numero,"es:",suma_digitos)
    
    sumaTotal += numero
    sumaDigitosTotal += suma_digitos

print("Resultados finales:")
print("La suma total de los números ingresados es:",sumaTotal)
print("La suma total de los dígitos de todos los números es:",sumaDigitosTotal)
