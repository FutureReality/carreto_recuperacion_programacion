from producto import Producto
from carrito import Carrito
from collections import OrderedDict
import json

class GestorComandas:
    def __init__(self):
        self.inventario = OrderedDict()
        self.carrito = Carrito()
        self.categorias = {"e": "electronica", "r": "ropa", "a": "alimentacion"}

    def agregar_producto(self):
        try:
            print("agregando producto, completa todos los camppos correctamente")
            codigo_num = input("codigo numerico (4 digitos): ").strip()

            if not codigo_num.isdigit() or len(codigo_num) != 4:
                print("error: el codigo debe ser un numero de 4 digitos.")
                return

            codigo = f"prod-{codigo_num}"

            if codigo in self.inventario:
                print(f"error: ya existe un producto con el codigo {codigo}.")
                return

            nombre = input("nombre: ")
            precio = float(input("precio: "))
            stock = int(input("stock: "))
            categoria_input = input("categoria (e)lectronica, (r)opa, (a)limentacion: ").lower().strip()

            if categoria_input in self.categorias:
                categoria = self.categorias[categoria_input]
            else:
                print("error: categoria no valida. debe ser e, r o a.")
                return

            nuevo = Producto(codigo, nombre, precio, stock, categoria)
            self.inventario[codigo] = nuevo
            print(f"producto {codigo} agregado correctamente.")
        except Exception as e:
            print("error:", e)

    def eliminar_producto(self):
        try:
            codigo = input("codigo del producto a eliminar: ").strip().lower()
            if codigo in self.inventario:
                del self.inventario[codigo]
                print("producto eliminado.")
            else:
                print("error: no existe producto con ese codigo.")
        except Exception as e:
            print("error:", e)

    def buscar_producto(self):
        try:
            termino = input("introduce nombre o parte del nombre: ").lower()
            encontrados = [p for p in self.inventario.values() if termino in p.nombre.lower()]
            if encontrados:
                for p in encontrados:
                    print(p)
            else:
                print("error: no se encontro producto.")
        except Exception as e:
            print("error:", e)

    def ver_carrito(self):
        try:
            if not self.carrito.contenido:
                print("el carrito esta vacio.")
                
            else:
                for p in self.carrito.contenido:
                    print(p)
                descuento = Carrito.aplicar_descuentos(self.carrito.contenido)
                print(f"descuento aplicado: {descuento:.2f} eur")
                
        except Exception as e:
            print("error:", e)

    def agregar_al_carrito(self):
        try:
            codigo = input("codigo del producto a agregar al carrito: ").strip().lower()
            if codigo in self.inventario:
                producto = self.inventario[codigo]
                self.carrito.agregar_al_carrito(producto)
            else:
                print("error: no existe producto con ese codigo.")
        except Exception as e:
            print("error:", e)

    def generar_factura(self):
        try:
        
            factura = {
                "fecha_hora": self.carrito.fecha_hora.isoformat(),
                "productos": [],
                "descuento": 0,
                "total_final": 0
            }

            total = 0
            for p in self.carrito.contenido:
                factura["productos"].append({
                    "codigo": p.codigo,
                    "nombre": p.nombre,
                    "precio": p.precio
                })
                total += p.precio

            descuento = Carrito.aplicar_descuentos(self.carrito.contenido)
            factura["descuento"] = descuento
            factura["total_final"] = total - descuento

            with open("facturas.json", "a", encoding="utf-8") as f:
                json.dump(factura, f, ensure_ascii=False, indent=4)
                f.write("\n")

            print("factura generada correctamente.")
        except Exception as e:
            print("error:", e)
