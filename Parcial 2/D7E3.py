def suma_digitos(numero):
    suma = 0
    numero = abs(numero)
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    return suma

while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        print("¡Adiós!")
        break
    resultado = suma_digitos(numero)
    print("La suma de los dígitos",numero,"es:",resultado)
