def serieFibonacci(numero):
    if(numero==0 or numero==1):
        return 1
    else:
        return serieFibonacci(numero-1)+serieFibonacci(numero-2)
    
while True:
    n=int(input("Ingrese un número: "))
    if(n>=1):
        break

for i in range(n):
    print(serieFibonacci(i))