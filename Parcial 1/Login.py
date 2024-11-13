#Login

user=input("Ingrese su usuario: ")
user_login="felipe"
password=input("Ingrese su contraseña: ")
password_login="felipe123"

if user==user_login and password==password_login:
    print("Bienvenido al sistema de ventas!")
else:
    print ("Credenciales incorrectas, vuelva a intentar.")
    user=input("Ingrese su usuario: ")
    password=input("Ingrese su contraseña: ")
if user==user_login and password==password_login:
    print("Bienvenido al sistema de ventas!")
else: 
    print("Usuario bloqueado.")