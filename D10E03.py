def calcularFactorial(numero):
    if numero==0:
        return 1
    if numero>1:
        numero=numero*calcularFactorial(numero-1)
    return numero

numeroX=int(input("Ingrese el numero de su factorial: "))
print("El resultado es: ",calcularFactorial(numeroX))