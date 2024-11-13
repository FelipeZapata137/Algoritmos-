#uso de match

estado_http=input("Introduzca el código de error: ")
match estado_http:
    case"200":
        print("Todo OK.")
    case"301":
        print("Movimiento permanente de la página.")
    case"302":
        print("Movimiento temporal de la página.")
    case"404":
        print("Página o recurso no encontrado.")
    case"500":
        print("Error interno del servidor.")
    case"503":
        print("Servicio no disponible.")
    case _:
        print("El estado no existe.")