def menu():
    print("----------LA FAVORITA----------")
    print("")
    print("Menú de opciones:")
    print("1. Ingresar productos al carrito de compras")
    print("2. Facturar")
    print("3. Salir")
    opcion=int(input("Ingresar opción: "))
    match opcion:
        case 1:
            return ingresarProductos()
        case 2:
            return facturar()
        case 3:
            return salir()

def ingresarProductos():
    global productos
    productos=list("")
    cnt=0
    resp=input("¿Desea seguir ingresando artículos?: ")
    while resp=="si" or resp=="SI":
        productos.append(input("Ingrese el nombre del artículo: "))
        resp=input("¿Desea seguir ingresando artículos?: ")

    print("Su lista de compras es:")
    for p in productos:
        cnt+=1
        print(cnt,p)
    menu()

def facturar():
    b=0
    cnt=0
    cnt2=0
    productos=list()
    cupon="navidad-epn"
    suma=0
    precio=float
    tamanio=int(input("Ingrese la cantidad de productos que ingresó: "))
    print("Ingrese su lista de compras:")
    for i in range(tamanio):
        cnt+=1
        productos.insert(i,input(f"Ingrese el producto {i+1}: "))
    print("¿Tiene cupones activos")
    print("1. Si.")
    print("2. No")
    alternativa=int(input("Ingrese su respuesta(si/no): "))
    match alternativa:
        case 1:
            cuponIngreso=input("Ingrese el código del cupón: ")
            while b<1:
                if cuponIngreso==cupon:
                    b+=1
                else:
                    print("Código inválido, vuelva a ingresar.")
                    cuponIngreso=input("Ingrese el código del cupón: ")
                for n in range(tamanio):
                    print("Ingrese el precio de",productos[n])
                    precio=float(input())
                    suma+=(precio/2)
                        
        case 2:
            for n in range(tamanio):
                print("Ingrese el precio de",productos[n])
                precio=float(input())
                suma+=precio
        case _:
            print("Opción inválida, se le reiniciará la facturación")
            facturar()
    print("El valor a pagar es:",suma)
    menu()

def salir():
    print("Gracias por usar nuestro sistema, somos La Favorita, y somos tu favorita, ten un buen día!")

def login():
    email1="felipe@favorita.com"
    password1="zapata"
    email2="javier@favorita.com"
    password2="gonzalez"
    correo=str
    clave=str
    a=0

    while (a<1):
        correo=input("Ingrese su correo: ")
        clave=input("Ingrese su contraseña: ")
        if(correo==email1 and clave==password1 or correo==email2 and clave==password2):
            a+=1
            menu()
        else:
            print("Credenciales incorrectas, vuelva a ingresar.")

print("--------------LA FAVORITA--------------")
login()