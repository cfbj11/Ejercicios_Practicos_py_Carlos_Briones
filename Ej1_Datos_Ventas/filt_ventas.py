#   FILTRAR LAS VENTAS

import datos_ventas as dv

umbral = 10
ventas_filtradas = list(filter(lambda venta: venta["cantidad"] > umbral, dv.ventas))