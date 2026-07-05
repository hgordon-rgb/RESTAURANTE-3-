class Producto:
    """
    Clase padre que representa un producto general del restaurante.
    """

    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.disponible = disponible

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.__precio = precio  # Encapsulación

    def obtener_precio(self):
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            print("Error: el precio debe ser mayor que cero.")
        else:
            self.__precio = nuevo_precio

    def mostrar_informacion(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.__precio}")
        print(f"Disponible: {self.disponible}")