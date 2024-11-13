def cociente():
    n1=float(input("Ingrese un número: "))
    n2=float(input("Ingrese otro número: "))
    if n2!=0:
        print("El cociente es: ",(n1/n2))
    else:
        print("No existe división para cero.")

cociente()