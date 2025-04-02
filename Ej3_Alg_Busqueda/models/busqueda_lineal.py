#   BUSQUEDA LINEAL

def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice
    return -1