productos = []
cantidades = []


def registrar_producto():
    nombre = input("¿Cómo se llama el producto?: ").strip()
    if not nombre:
        print("¡Ey! El nombre no puede quedar vacío.")
        return

    if nombre in productos:
        print(
            "¡Ese producto ya está anotado! Mejor usa la opción de modificar la cantidad."
        )
        return

    try:
        cantidad = int(input("¿Cuántas unidades hay disponibles?: "))
        if cantidad < 0:
            print("No puedes poner cantidades negativas, ingresa un número válido.")
            return
    except ValueError:
        print("¡Ojo! Tienes que meter un número entero válido.")
        return

    productos.append(nombre)
    cantidades.append(cantidad)
    print(f"¡Listo! El producto '{nombre}' quedó registrado de una.")


def mostrar_inventario():
    if len(productos) == 0:
        print("Mmm, parece que por ahora no hay nada en el inventario.")
    else:
        print("\n--- ASÍ VA TU INVENTARIO ---")
        for i in range(len(productos)):
            print(f"{i + 1}. {productos[i]} — {cantidades[i]} unidades")


def buscar_producto():
    if len(productos) == 0:
        print("El inventario está vacío, no hay nada que buscar todavía.")
        return

    nombre = input("¿Qué producto andas buscando?: ").strip()
    if nombre in productos:
        indice = productos.index(nombre)
        print(
            f"¡Lo encontré! Producto: {productos[indice]} | Cantidad: {cantidades[indice]} unidades"
        )
    else:
        print(f"Uy, no encontré por ningún lado a '{nombre}' en el inventario.")


def modificar_cantidad():
    if len(productos) == 0:
        print("Todavía no hay productos para modificar.")
        return

    nombre = input("¿Cuál producto quieres modificar?: ").strip()
    if nombre in productos:
        indice = productos.index(nombre)
        print(f"Actualmente '{nombre}' tiene {cantidades[indice]} unidades.")
        try:
            nueva_cantidad = int(input("¿Cuál va a ser la nueva cantidad?: "))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa, intenta de nuevo.")
                return
            cantidades[indice] = nueva_cantidad
            print("¡Quedó listo! La cantidad se actualizó sin problema.")
        except ValueError:
            print("¡Ups! Tienes que ingresar un número entero.")
    else:
        print(f"Mmm, '{nombre}' no aparece por ningún lado.")


def eliminar_producto():
    if len(productos) == 0:
        print("No hay nada que eliminar, el inventario está vacío.")
        return

    nombre = input("¿Qué producto quieres borrar del mapa?: ").strip()
    if nombre in productos:
        indice = productos.index(nombre)
        productos.pop(indice)
        cantidades.pop(indice)
        print(f"¡Chao! '{nombre}' fue eliminado del inventario.")
    else:
        print(f"Ese producto ('{nombre}') no existe, así que no se puede borrar.")


def mostrar_resumen():
    if len(productos) == 0:
        print("No hay resumen porque el inventario está a cero.")
        return

    total_diferentes = len(productos)
    max_cantidad = max(cantidades)
    indice_max = cantidades.index(max_cantidad)
    producto_mayor = productos[indice_max]

    print("\n--- RESUMEN RÁPIDO ---")
    print(f"Tienes {total_diferentes} productos diferentes registrados.")
    print(
        f"El que más abunda es '{producto_mayor}' con {max_cantidad} unidades."
    )


def menu():
    while True:
        print("\n==============================")
        print("    GESTOR DE INVENTARIO")
        print("==============================")
        print("1. Registrar un producto nuevo.")
        print("2. Ver todo el inventario.")
        print("3. Buscar un producto.")
        print("4. Cambiar la cantidad de un producto.")
        print("5. Borrar un producto.")
        print("6. Ver cuántos productos diferentes hay.")
        print("7. Ver cuál producto tiene más stock.")
        print("8. Salir del programa.")

        opcion = input("Elige una opción (1-8): ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            if len(productos) == 0:
                print("El inventario está vacío.")
            else:
                print(
                    f"\nTienes {len(productos)} productos diferentes registrados."
                )
        elif opcion == "7":
            if len(productos) == 0:
                print("El inventario está vacío.")
            else:
                max_cantidad = max(cantidades)
                indice_max = cantidades.index(max_cantidad)
                print(
                    f"\nEl que más abunda es '{productos[indice_max]}' con {max_cantidad} unidades."
                )
        elif opcion == "8":
            print("¡Saliendo del programa! Nos vemos pronto.")
            break
        else:
            print("¡Esa opción no existe! Elige un número del 1 al 8.")


if __name__ == "__main__":
    menu()