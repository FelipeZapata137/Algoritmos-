nota=float
suma=0
cnt=0
while nota!=0:
    nota=float(input("Ingrese una nota: "))
    suma+=nota
    cnt+=1

promedio=suma/(cnt-1)
print("El promedio es",promedio)