def calcular_factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial


contador = 0
    
print("Ingresa números para calcular su factorial. Para terminar, ingresa -1.")
    
while True:
    numero = int(input("Ingresa un número entero positivo: "))
        
    if numero == -1:
        break
        
    if numero < 0:
        print("Por favor, ingresa un número no negativo.")
    else:
        contador += 1
        factorial = calcular_factorial(numero)
        print("El factorial de",numero,"es",factorial)

print("Has ingresado un total de", contador, "números.")