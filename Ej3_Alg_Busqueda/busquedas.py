#   ARCHIVO PRINCIPAL

from models.busqueda_lineal import busqueda_lineal as bl
from models.busqueda_binaria import busqueda_binaria as bb

datos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
print("Lista:", datos)
objetivo = int(input("Ingrese el número a buscar: "))

#   RESULTADOS BUSQUEDA LINEAL

resultado_lineal = bl(datos, objetivo)
print("\nBusqueda lineal:")
if resultado_lineal != -1:
    print(f"Elemento {objetivo} encontrado en la posición {resultado_lineal}.")
else:
    print(f"Elemento {objetivo} no encontrado.")

#   RESULTADOS BUSQUEDA BINARIA

resultado_binario = bb(datos, objetivo)
print("\nBusqueda binaria:")
if resultado_binario != -1:
    print(f"Elemento {objetivo} encontrado en la posición {resultado_binario}.")
else:
    print(f"Elemento {objetivo} no encontrado.")