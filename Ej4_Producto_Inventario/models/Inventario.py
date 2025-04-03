#   INVENTARIO

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None
    
    def eliminar_producto(self, codigo, nombre=None, precio=None, cantidad=None):
        producto = self.buscar_producto(codigo)
        if producto:
            if nombre:
                producto.nombre = nombre
            if precio:
                producto.precio = precio
            if cantidad:
                producto.cantidad = cantidad
            return True
        return False
    
    def elimininar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacio.")