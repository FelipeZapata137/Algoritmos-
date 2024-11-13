import math

def constantes():
    cte=input("Inserte el nombre de su constante favorita (pi/euler): ")
    match cte:
        case 'pi': print("El valor es ",math.pi)
        case 'euler': print("El valor es ",math.e)

constantes()