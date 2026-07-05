class Restaurante:
    """
    Clase de servicio encargada de administrar productos.
    """

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("\n===== PRODUCTOS DEL RESTAURANTE =====")

        for producto in self.productos:
            producto.mostrar_informacion()  # Polimorfismo