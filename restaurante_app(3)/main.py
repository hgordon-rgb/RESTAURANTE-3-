from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():

    restaurante = Restaurante()

    # Platillos
    platillo1 = Platillo(
        "Arroz con Pollo",
        5.50,
        True,
        650
    )

    platillo2 = Platillo(
        "Encebollado",
        4.75,
        True,
        550
    )

    # Bebidas
    bebida1 = Bebida(
        "Jugo de Naranja",
        2.00,
        True,
        350
    )

    bebida2 = Bebida(
        "Coca Cola",
        1.50,
        True,
        500
    )

    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    restaurante.mostrar_productos()


if __name__ == "__main__":
    main()