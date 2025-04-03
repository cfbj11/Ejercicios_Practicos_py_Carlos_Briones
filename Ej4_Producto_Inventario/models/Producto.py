#   PRODUCTO

class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Código: {self.codigo}, Precio: ${self.precio}, Cantidad: {self.cantidad}"