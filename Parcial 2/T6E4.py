user="Felipe Zapata"
password="175367"

cnt=1
while cnt<=3:
    userLog=input("Ingrese su usuario: ")
    passwordLog=input("Ingrese su clave: ")
    if userLog==user and passwordLog==password:
        print("Bienvenido al sistema. ")
        break
    else:
        print("Información inválida, inténtelo una vez más.")
        cnt+=1