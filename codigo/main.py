from gestorcomandas import GestorComandas

def menu():
    gestor = GestorComandas()
    
    while True:
        print("\nmenu:")
        print("(a)gregar, (e)liminar, (b)uscar, (v)er carrito, (f)acturar, (c)argar al carrito, (s)alir")
        opcion = input("seleccione una opcion: ").lower()

        if opcion == "a":
            gestor.agregar_producto()
        elif opcion == "e":
            gestor.eliminar_producto()
        elif opcion == "b":
            gestor.buscar_producto()
        elif opcion == "v":
            gestor.ver_carrito()
        elif opcion == "f":
            gestor.generar_factura()
        elif opcion == "c":
            gestor.agregar_al_carrito()
        elif opcion == "s":
            break
        else:
            print("error: esa opcion no es valida.")

if __name__ == "__main__":
    menu()
