#PUNTO 1 DEL TALLER FINAL

import os
inventario = []
while True:
    os.system("cls")
    print("\n---CONTROL DE INVENTARIO Y COSTOS👷🏻‍♀️ ---")
    print("1. Agregar producto")
    print("2. Ver productos del inventario")
    print("3. Eliminar producto")
    print("4. Promedio subtotales y sumar totales")
    print("5. salir (^///^)")
    opcion = input("👉🏻Seleccione una opción: \n")
    
    match opcion:
            case "1":
                nombre = input("Ingrese el nombre del producto: \n").strip()
                cantidad = int(input("Ingrese la cantidad del producto: \n"))
                precio_1 = float(input(f"Precio del producto unitario {nombre}: \n"))
                inventario.append([nombre, cantidad, precio_1])
                print(f"Producto {nombre} agregado exitosamente")
                input("Presione una tecla para continuar.")
            case "2":
                if len(inventario)==0:
                    print("No hay productos registrados con esta información")
                else:
                    print("\n ---LISTA DE PRODUCTOS🛒---")
                    for i, inv in enumerate(inventario, 1):
                        subtotal = inv[1] * inv[2]
                        print(f"{i}. Nombre: {inv[0]} | Cantidad: {inv[1]} | Precio U.: ${inv[2]:.2f} | Subtotal: {subtotal:.2f}")
                input("Presione una tecla para continuar.")
            case "3":
                nombreEliminar = input("Ingrese el nombre del producto por eliminar: ").strip()
                eliminado = False
                for inv in inventario:
                    if inv[0].lower() == nombreEliminar.lower():
                        inventario.remove(inv)
                        print(f"El producto {nombreEliminar} fue eliminado")
                        eliminado = True
                        break
                if not eliminado:
                    print("Producto no encontrado")
                input("Presione una tecla para continuar.")
            case "4":
                print("--SUBTOTALES Y SUMA TOTAL--")
                if not inventario:
                    print("No hay productos regristrados")
                else:
                    sumacompleta = sum(inv[1] * inv[2] for inv in inventario)
                promedio = sumacompleta / len(inventario)
                print(f"Suma total del inventario: ${sumacompleta:.2f}")
                print(f"Promedio de costo por subtotal: ${promedio:.2f}")
                input("Presione una tecla para continuar.")
            case "5":
                print("Saliendo de la interfaz (☆▽☆)")
                break
            case _:
                print("Opción no valida ಥ_ಥ")
                input("Presione una tecla para continuar.")