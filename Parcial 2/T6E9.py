lista1=[5, 1, 9, 2, 7, 4]
numero=int(input("Ingrese el numero a buscar: "))
cnt=0
for l in lista1:
    cnt+=1
    if l==numero:
        print("Si está en la lista.")
        break
if cnt==len(lista1):
    print("Ese numero no está en la lista")