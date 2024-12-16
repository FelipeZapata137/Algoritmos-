def quick_sort(array):
    # Caso base: Si el array tiene 0 o 1 elemento, ya está ordenado
    if len(array) <= 1:
        return array

    # Elegir un pivote (normalmente el último elemento)
    pivot = array[-1]

    # Dividir en listas menores y mayores al pivote
    less_than_pivot = [x for x in array[:-1] if x <= pivot]
    greater_than_pivot = [x for x in array[:-1] if x > pivot]

    # Ordenar recursivamente y combinar
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


# Ejemplo de uso
if __name__ == "__main__":
    unsorted_list = [10, 7, 8, 1, 6, 3, 5]
    sorted_list = quick_sort(unsorted_list)
    print("Lista ordenada:", sorted_list)
