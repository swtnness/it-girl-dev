"""
Diccionarios Estructura Par Clave:Valor, son mutables y con claves unicas
{} -> Dictionary
"""

estudiante = {"Documento":103658792, "Nombre":"Vannesa", "Apellido":"Pulido", "Carrera": "Ingeniera de Sistemas", "Edad":22}
#ver diccionario
print(estudiante)
#ver un dato de una clave
carrera = estudiante.get("Carrera")
print(carrera)
claves = estudiante.keys()
print(claves)
valores = estudiante.values()
print(valores)
items = estudiante.items()
print(items)
#ciclo for
for clave, valor in estudiante.items():
    print(f"{clave.capitalize()}: {valor}")
    
#agregar dato al dicc
estudiante["Promedio"] = 4.7
print(estudiante)
#modificar valor
estudiante["Promedio"] = 4.8
print(estudiante)
#eliminar clave
estudiante.pop("Documento")
del estudiante["Promedio"]
print(estudiante)
#limpiar un dicc
estudiante.clear()