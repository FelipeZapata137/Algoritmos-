#notas

nota=float(input("Ingrese su nota:"))

if 0<=nota<5:
    print("Insuficiente.")
elif 5<=nota<7:
    print("Regular.")
elif 7<=nota<8:
    print("Bueno.")
elif 8<=nota<9:
    print("Muy Bueno.")
elif 9<=nota<10:
    print("Sobresaliente.")
elif 0>nota:
    print("Nota mal ingresada.")
else:
    print("Nota mal ingresada.")