"""
Tuplas no son mutables
() -> Tuple
"""
colores = ("Rosado", "Rojo", "Rosa pastel", "Amarillo")
#ver tupla
print(colores)
#ciclo
for item in colores:
    print(item)
#ver una posicion
print(colores[2])
#tamaño de la tupla
print(len(colores))
#buscar un item en la tupla
print("Marino" in colores)
#convertir una tupla a una lista
milista = list(colores)
#convetir una lista en una tupla
miTupla = tuple(milista)