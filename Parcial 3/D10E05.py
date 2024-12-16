def ordenarLista(lista):
    if len(lista) <= 1:
        return lista
    
    centinela=lista[0]
    
    menoralCentinela=[x for x in lista[1:] if x<=centinela]
    mayoralCentinela=[x for x in lista[1:] if x>centinela]
    
    return ordenarLista(menoralCentinela) + [centinela] + ordenarLista(mayoralCentinela)

listaUno=[34, 7, 23, 32, 5, 62]
listaOrdenada=ordenarLista(listaUno)
print("Lista desordenada: ",listaUno)
print("Lista ordenada: ",listaOrdenada)