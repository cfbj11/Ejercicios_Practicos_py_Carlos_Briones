#   EJERCICIO 1: ANALISIS DE DATOS DE VENTAS

from functools import reduce
from collections import defaultdict

#   DATOS DE VENTAS

ventas = [
    {"producto": "A", "cantidad": 5, "precio": 8},
    {"producto": "B", "cantidad": 6, "precio": 5},
    {"producto": "C", "cantidad": 2, "precio": 4},
    {"producto": "D", "cantidad": 3, "precio": 8},
    {"producto": "E", "cantidad": 4, "precio": 5},
]

class DatosVentas:
    def __init__(self, ventas):
        self.ventas = ventas

#   METODO PARA OBTENER VENTAS POR PRODUCTO

class CalcVentas:
    def __init__(self, ventas):
        self.ventas = ventas
    
    def calcular_ventas(self, venta):
        return venta["cantidad"] * venta["precio"]
    
    def total_general(self):
        totales_ventas = list(map(self.calcular_ventas, self.ventas))
        return reduce(lambda x, y: x + y, totales_ventas)

#   METODO PARA FILTRAR VENTAS POR CANTIDAD

class FiltVentas:
    def __init__(self, ventas):
        self.ventas = ventas

    def filtrar_ventas(self, umbral):
        return list(filter(lambda venta: venta["cantidad"] > umbral, self.ventas))

#   METODO PARA CALCULAR PROMEDIO DE VENTAS POR PRODUCTO

class PromedioVentas:
    def __init__(self, ventas):
        self.ventas = ventas
    
    def agrupar(self):
        ventas_por_producto = defaultdict(list)
        for venta in self.ventas:
            ventas_por_producto[venta["producto"]].append(venta)
        return ventas_por_producto
    
    def calcular_promedio(self):
        ventas_por_producto = self.agrupar()
        promedios = {}

        for producto, ventas in ventas_por_producto.items():
            total_producto = reduce(lambda x, y: x + (y["cantidad"] * y["precio"]), ventas, 0)
            cantidad_producto = reduce(lambda x, y: x + y["cantidad"], ventas, 0)
            promedio_producto = total_producto / cantidad_producto if cantidad_producto > 0 else 0
            promedios[producto] = promedio_producto
        
        return promedios

#   INICIALIZAR CLASES

datos_ventas = DatosVentas(ventas)
calc_ventas = CalcVentas(ventas)
filt_ventas = FiltVentas(ventas)
promedio_ventas = PromedioVentas(ventas)

#   CALCULAR RESULTADOS

total = calc_ventas.total_general()
umbral = 0
ventas_filtradas = filt_ventas.filtrar_ventas(umbral)
promedios = promedio_ventas.calcular_promedio()

#   IMPRIMIR RESULTADOS

print("Analisis de datos de ventas:")
print(f"\nTotal general de ventas: {total}")
print(f"\nVentas filtradas (cantidad > {umbral}):")
for venta in ventas_filtradas:
    print(venta)
print("\nPromedio de ventas por producto:")
for producto, promedio in promedios.items():
    print(f"Producto {producto}: {promedio:.2f}")