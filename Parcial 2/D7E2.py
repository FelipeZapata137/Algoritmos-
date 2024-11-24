def doblar_valor(lista):
    return [elemento * 2 for elemento in lista]

lista1 = [1, 2, 3, 4, 5]
doblar_valor(lista1)
print("Lista original:", lista1)
print("Lista doblada:", doblar_valor(lista1))