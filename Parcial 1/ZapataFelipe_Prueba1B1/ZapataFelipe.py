
print("Por favor, ingresa en el sistema para acceder a los servicios del Bar.")
user="Felipe Zapata"
userLog=str(input("Ingrese su usuario: "))
password=17536
passwordLog=int(input("Ingrese su contraseña: "))
    
if (userLog==user and passwordLog==password):
    print("Bienvenido al Bar de la EPN.")
    print("Le ofrecemos 4 tipos de menús:")
    print("1. Almuerzo Politécnico - $2,75")
    print("2. Almuerzo Ejecutivo - $3,75")
    print("3. Churrasco - $4,25")
    print("4. Milanesa - $4,75")
    menu=str(input("Seleccione el tipo de menú que va a desear: "))
    match menu:
        case"1": 
            fn=float(input("¿Cuántos va a ordenar?: "))
            subT=fn*2.75
            print("El subtotal es: ",subT)
            pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))

            match pago:
                case"tarjeta":
                    print("Okey, su precio final es: ", subT*1.15)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case"efectivo":
                    print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case _:
                    print("Método de pago inválido.")
        case"2":
            fn=float(input("¿Cuántos va a ordenar?: "))
            subT=fn*3.75
            print("El subtotal es: ",subT)
            pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))

            match pago:
                case"tarjeta":
                    print("Okey, su precio final es: ", subT*1.15)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case"efectivo":
                    print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case _:
                    print("Método de pago inválido.")
        case"3":
            fn=float(input("¿Cuántos va a ordenar?: "))
            subT=fn*4.25
            print("El subtotal es: ",subT)
            pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))
            match pago:
                case"tarjeta":
                    print("Okey, su precio final es: ", subT*1.15)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case"efectivo":
                    print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case _:
                    print("Método de pago inválido.")
        case"4":
            fn=float(input("¿Cuántos va a ordenar?: "))
            subT=fn*4.75
            print("El subtotal es: ",subT)
            pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))
            match pago:
                case"tarjeta":
                    print("Okey, su precio final es: ", subT*1.15)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case"efectivo":
                    print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                    print("Gracias por su compra, tenga un excelente día! :D")
                case _:
                    print("Método de pago inválido.")
        case _:
            print("Menú no válido")
else:
    print("Credenciales incorrectas, por favor vuelva a intentarlo.")
    userLog=str(input("Ingrese su usuario: "))
    passwordLog=int(input("Ingrese su contraseña: "))
    if (userLog==user and passwordLog==password):
        print("Bienvenido al Bar de la EPN.")
        print("Le ofrecemos 4 tipos de menús:")
        print("1. Almuerzo Politécnico - $2,75")
        print("2. Almuerzo Ejecutivo - $3,75")
        print("3. Churrasco - $4,25")
        print("4. Milanesa - $4,75")
        menu=str(input("Seleccione el tipo de menú que va a desear: "))
        match menu:
            case"1": 
                fn=float(input("¿Cuántos va a ordenar?: "))
                subT=fn*2.75
                print("El subtotal es: ",subT)
                pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))
                match pago:
                    case"tarjeta":
                        print("Okey, su precio final es: ", subT*1.15)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case"efectivo":
                        print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case _:
                        print("Método de pago inválido.")
            case"2":
                fn=float(input("¿Cuántos va a ordenar?: "))
                subT=fn*3.75
                print("El subtotal es: ",subT)
                pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))
                match pago:
                    case"tarjeta":
                        print("Okey, su precio final es: ", subT*1.15)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case"efectivo":
                        print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case _:
                        print("Método de pago inválido.")
            case"3":
                fn=float(input("¿Cuántos va a ordenar?: "))
                subT=fn*4.25
                print("El subtotal es: ",subT)
                pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))
                match pago:
                    case"tarjeta":
                        print("Okey, su precio final es: ", subT*1.15)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case"efectivo":
                        print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case _:
                        print("Método de pago inválido.")
            case"4":
                fn=float(input("¿Cuántos va a ordenar?: "))
                subT=fn*4.75
                print("El subtotal es: ",subT)
                pago=str(input("¿De qué forma va a cancelar, efectivo o tarjeta?: "))
                match pago:
                    case"tarjeta":
                        print("Okey, su precio final es: ", subT*1.15)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case"efectivo":
                        print("Acérquese a la caja y cancele, su precio final es: ", subT*0.9)
                        print("Gracias por su compra, tenga un excelente día! :D")
                    case _:
                        print("Método de pago inválido.")
            case _:
                print("Menú no válido")
    else: print("Lo sentimos, su cuenta será bloqueada.")