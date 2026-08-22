"""CRUD Lógico de Datos
Hacer un programa que almacene los datos de los estudiantes
nombre y nota final en una lista debe de tener un menu de
opciones para agregar, mostrar datos, eliminar, mostrar
promedio de estudiantes y salir.
"""
import os
estudiantes = []
while True:
    os.system("cls")
    print("\n---👩‍💻SISTEMA DE ESTUDIANTES ---")
    print("1. Agregar estudiante")
    print("2. Ver estudiante con notas")
    print("3. Eliminar estudiante")
    print("4. Promedio general de notas de estudiante")
    print("5. salir (^///^)")
    opcion = input("👉🏻Seleccione una opción: \n")
    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del estudiante: \n").strip()
            nota = float(input(f"Nota final de {nombre}: \n"))
            estudiantes.append([nombre, nota])
            print(f"Estudiante {nombre} agregado exitosamente")
            input("Presione una tecla para continuar.")
        case "2":
            if len(estudiantes)==0:
                print("No hay estudiantes registrados")
            else:
                print("\n ---LISTA DE ESTUDIANTES👧🏻👦🏻---")
                for i, est in enumerate(estudiantes, 1):
                    print(f"{i}. Nombre: {est[0]} | Nota Final: {est[1]}")
            input("Presione una tecla para continuar.")
        case "3":
            nombreEliminar = input("Ingrese el nombre del estudiante por eliminar: ").strip()
            eliminado = True
            for est in estudiantes:
                if est[0].lower() == nombreEliminar.lower():
                    estudiantes.remove(est)
                    print(f"El estudiante {nombreEliminar} fue eliminado")
                    eliminado = True
                    break
            if not eliminado:
                print("Estudiante no encontrado")
            input("Presione una tecla para continuar.")
        case "4":
            if not estudiantes:
                print("No hay estudiantes regristrados")
            else:
                suma = sum(est[1] for est in estudiantes)
                promedio = suma / len(estudiantes)
                print(f"Promedio general de notas: {promedio:.2f}")
            input("Presione una tecla para continuar.")
        case "5":
            print("Saliendo de la interfaz (☆▽☆)")
            break
        case _:
            print("Opción no valida `(*>﹏<*)′")
            input("Presione una tecla para continuar.")