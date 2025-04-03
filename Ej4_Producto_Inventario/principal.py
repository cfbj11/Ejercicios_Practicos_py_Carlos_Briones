#   EJERCICIO 4 : GESTION DE PRODUCTOS E INVENTARIO

from Ej4_Producto_Inventario.models import Producto, Inventario

def main():
    p1 = Producto("001", "Laptop", 1500, 10)
    p2 = Producto("002", "Smartphone", 800, 20)
    p3 = Producto("003", "Tablet", 600, 15)

    inventario = Inventario()

    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)
    inventario.agregar_producto(p3)

    print("Inventario inicial:")
    inventario.mostrar_inventario()

    respuesta = input(print("Que accion desea realizar?: \n1. Agregar producto\n2. Actualizar producto\n3. Eliminar producto"))
    if respuesta == "1":
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))

        nuevo_producto = Producto(codigo, nombre, precio, cantidad)
        inventario.agregar_producto(nuevo_producto)
        print("Producto agregado exitosamente.")
    if respuesta == "2":
        codigo = input("Ingrese el código del producto a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del producto: ")
        precio = int(input("Ingrese el nuevo precio del producto: "))
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))

        inventario.actualizar_producto(codigo, nombre, precio, cantidad)
        print("Producto actualizado exitosamente.")
    if respuesta == "3":
        codigo = input("Ingrese el código del producto a eliminar: ")
        inventario.eliminar_producto(codigo)
        print("Producto eliminado exitosamente.")

    if __name__ == "__main__":
        main()