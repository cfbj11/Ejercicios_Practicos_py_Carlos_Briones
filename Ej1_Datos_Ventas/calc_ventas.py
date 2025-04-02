#   CALCULAR TOTAL DE VENTAS

from functools import reduce
import datos_ventas as dv

def calcular_ventas(venta):
    return venta["cantidad"] * venta["precio_unitario"]

totales_ventas = list(map(calcular_ventas, dv.ventas))

total_general = reduce(lambda x, y: x + y, totales_ventas)