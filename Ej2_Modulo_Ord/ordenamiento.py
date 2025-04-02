#   EJERCICIO 2: MODULO DE ORDENAMIENTO

import bubble_sort as bs

def main():
    lista = [47, 28, 59, 18, 8, 34, 52, 78, 96, 11, 40, 67, 89, 21, 43]
    print("Lista original:", lista)

    lista_ordenada = bs.bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()