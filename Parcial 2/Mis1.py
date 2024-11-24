def siguiente_mayor(lista):
    resultado = [] 

    for i in range(len(lista)):
        mayor = -1
        for j in range(i + 1, len(lista)):
            if lista[j] > lista[i]:
                mayor = lista[j]
                break
        resultado.append(mayor) 
    return resultado

numeros = [4, 5, 2, 10, 8]
print(siguiente_mayor(numeros))

numeros2 = [7, 3, 1]
print(siguiente_mayor(numeros2))