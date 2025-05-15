import re

class Producto:
    def __init__(self, codigo, nombre, precio, stock, categoria):
        if not re.match(r"prod-\d{4}", codigo):
            raise ValueError(f"codigo {codigo} no valido. formato prod-xxxx requerido")
            
        if categoria not in ["electronica", "ropa", "alimentacion"]:
            raise ValueError(f"categoria {categoria} no valda.")
            
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.precio} eur - stock: {self.stock} - categoria: {self.categoria}"
