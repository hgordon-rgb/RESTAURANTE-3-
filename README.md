# Tarea Semana 6
## Aplicación de herencia, encapsulación y polimorfismo

### Estudiante
Gordon Ortega Henri Daniel

### Descripción
Este proyecto implementa un sistema básico de restaurante utilizando Programación Orientada a Objetos en Python. El sistema administra productos de un restaurante mediante una jerarquía de clases.

### Estructura del proyecto

restaurante_app/
│
├── modelos/
│   ├── producto.py
│   ├── platillo.py
│   └── bebida.py
│
├── servicios/
│   └── restaurante.py
│
└── main.py

### Relación de herencia

Producto
├── Platillo
└── Bebida

La clase Producto es la clase padre y las clases Platillo y Bebida son clases hijas.

### Encapsulación

El atributo precio fue encapsulado mediante:

```python
self.__precio