#   EJERCICIO 5: PROCESAMIENTO DE PEDIDOS Y CLIENTES

class Cliente:
    def __init__(self, cliente_id, nombre, contacto):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.contacto = contacto
    
    def obtener_info(self):
        return f"ID: {self.cliente_id}, Nombre: {self.nombre}, Contacto: {self.contacto}"
    
    def calcular_descuento(self, total):
        return 0
    
class ClienteVip(Cliente):
    def __init__(self, cliente_id, nombre, contacto, nivel_vip):
        super().__init__(cliente_id, nombre, contacto)
        self.nivel_vip = nivel_vip

    def obtener_info(self):
        return f"{super().obtener_info()}, Nivel VIP: {self.nivel_vip}"

    def calcular_descuento(self, total):
        if self.nivel_vip == "Alto":
            return total * 0.2
        elif self.nivel_vip == "Medio":
            return total * 0.1
        else:
            return 0
        
class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.total = sum([producto['precio'] for producto in productos])

    def calcular_total_con_descuento(self):
        descuento = self.cliente.calcular_descuento(self.total)
        total_con_descuento = self.total - descuento
        return total_con_descuento
    
    def mostrar_pedido(self):
        productos_str = "\n".join([f"{producto['nombre']} - ${producto['precio']}" for producto in self.productos])
        total_con_descuento = self.calcular_total_con_descuento()
        return f"Pedido de {self.cliente.nombre} (ID: {self.cliente.cliente_id}):\n" \
               f"Productos:\n{productos_str}\nTotal: ${self.total}\n" \
               f"Total con descuento: ${total_con_descuento}"
    
cliente_regular = Cliente(cliente_id = 1, nombre = "Alejandro Ramirez", contacto = "aleramirez@gmail.com")
cliente_vip = ClienteVip(cliente_id = 2, nombre = "Ana Perez", contacto = "anap@gmail.com", nivel_vip = "Alto")

productos = [
    {"nombre": "Lampara", "precio": 50},
    {"nombre": "Secadora", "precio": 80},
    {"nombre": "Cafetera", "precio": 40}
]

pedido_regular = Pedido(cliente = cliente_regular, productos = productos)
pedido_vip = Pedido(cliente = cliente_vip, productos = productos)

print(pedido_regular.mostrar_pedido(), end="\n\n")
print(pedido_vip.mostrar_pedido())