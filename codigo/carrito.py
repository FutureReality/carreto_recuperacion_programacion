from datetime import datetime
from collections import defaultdict

class Carrito:
    def __init__(self):
        self.contenido = []
        self.fecha_hora = datetime.now()

    def agregar_al_carrito(self, producto):
        if producto.stock <= 0:
            print(f"error: no hay stock suficiente del producto {producto.codigo}.")
            return
        producto.stock -= 1
        self.contenido.append(producto)
        print(f"producto {producto.codigo} anyadido al carrito. stock restante: {producto.stock}")

    @staticmethod
    def aplicar_descuentos(contenido):
        agrupados = defaultdict(list)
        for producto in contenido:
            agrupados[producto.categoria].append(producto)

        descuento_total = 0
        for productos in agrupados.values():
            if len(productos) >= 3:
                subtotal = sum(p.precio for p in productos)
                descuento_total += subtotal * 0.15

        return descuento_total
