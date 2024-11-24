def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial


print("Calculadora de factorial")
numero = int(input("Ingresa un número entero positivo: "))
    
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = calcular_factorial(numero)
    print("El factorial de",numero,"es",resultado)