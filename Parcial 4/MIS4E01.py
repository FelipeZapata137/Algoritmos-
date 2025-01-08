def agregarCliente():
    print("\tAGREGAR CLIENTE")
    valor={}
    valor["nombre"]=input("Ingrese su nombre: ")
    valor["direccion"]=input("Ingrese su dirección: ")
    valor["telefono"]=input("Ingrese su teléfono: ")
    valor["correo"]=input("Ingrese su correo: ")
    preferencia=input("¿Es usted usuario preferente?(si/no): ")
    match preferencia:
        case "si": preferencia=True
        case "no": preferencia=False
        case _:
            print("Opción inválida")
            agregarCliente()
        
    valor["preferente"]=preferencia

    clave=int(input("Ingrese su número de cédula: "))
    clientes[clave]=valor
    print("Cliente agregado exitosamente.")

    menu()
    return clientes

def eliminarCliente(clientes):
    print("\tELIMINAR CLIENTE.")
    clave=int(input("Ingrese el número de cédula de quien será borrado: "))
    del clientes[clave]
    print("El usuario ha sido eliminado con éxito.")
    menu()
    return clientes

def mostrarCliente(clientes):
    print("\tMOSTRAR CLIENTE.")
    clave=int(input("Ingrese el número de cédula del cliente que quiere ver: "))
    print(clientes[clave])
    menu()
    return clientes

def listarClientes(clientes):
    print("\tLISTA DE CLIENTES.")
    a=1

    for dni, datos in clientes.items():
        print(f"{a}. Cliente: {datos["nombre"]}.\t ID: {dni}")
        a+=1
    
    menu()
    return clientes

def listarClientesPreferentes(clientes):
    print("\tLISTA DE CLIENTES PREFERENTES.")
    b = 1
    for dni, datos in clientes.items():
        if datos["preferente"]:
            print(f"{b}. Cliente: {datos['nombre']}. \t ID: {dni}")
            b += 1
    if b == 1:
        print("No hay clientes preferentes.")
    menu()
    return clientes

def terminar():
    print("Gracias por usar nuestros servicios, buen día!")

def menu():
    print("1. Agregar Cliente.")
    print("2. Eliminar Cliente.")
    print("3. Mostrar Cliente.")
    print("4. Listar Todos los Clientes.")
    print("5. Listar Clientes Preferentes.")
    print("6. Terminar.")
    opcion=int(input("Seleccione una opción (1 a 6): "))

    match opcion:
        case 1: agregarCliente()
        case 2:
            if len(clientes)==0:
                print("No se han agregado clientes todavía.")
                menu()
            else:
                eliminarCliente(clientes)
        case 3:
            if len(clientes)==0:
                print("No se han agregado clientes todavía.")
                menu()
            else:
                mostrarCliente(clientes)
        case 4:
            if len(clientes)==0:
                print("No se han agregado clientes todavía.")
                menu()
            else:
                listarClientes(clientes)
        case 5:
            if len(clientes)==0:
                print("No se han agregado clientes todavía.")
                menu()
            else:
                listarClientesPreferentes(clientes)
        case 6: terminar()

clientes={}
print("\t Bienvenido al sistema de FelipeZapata.inc")
menu()