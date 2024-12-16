def restarValor(numero):
    numero -=1
    if numero>0:
        print(numero)
        restarValor(numero)
    else:
        print("Fin.")

numeroX=int(input("Ingrese un numero entero: "))
restarValor(numeroX)