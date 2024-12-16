def insertion_sort(arr):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Guardamos el valor actual y el índice anterior
        current_value = arr[i]
        j = i - 1
        
        # Desplazamos los elementos que sean mayores al valor actual
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertamos el valor actual en su posición correcta
        arr[j + 1] = current_value

    return arr

# Ejemplo de uso
numeros = [5, 3, 8, 6, 2]
print("Arreglo original:", numeros)
print("Arreglo ordenado:", insertion_sort(numeros))