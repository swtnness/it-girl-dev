"""
Listas son mutables
[] -> List
"""

frutas = ["Mango", "Fresa", "Papaya", "Kiwi", "Coco"]
#agregar item a la lista
frutas.append("Banano")
frutas.append("Pitalla")
frutas.append("Mora")
#ver la lista
print(frutas)

#ver la lista de manera estetica con for
for item in frutas:
    print(item)
#ver un dato de la lista
print(frutas[2])
#agregar una fruta despues de cualquier otra
frutas.insert(2, "Cereza")
print(frutas)
#eliminar un dato de la lista
frutas.remove("")
frutas.pop() #elimina el ultimo
frutas.pop(0) #elimina un dato del indice de la lista
#modifica un dato de la lista
print(frutas)
frutas[0] = "Cherry"
print(frutas)
#buscar un item por indice
indice = frutas.index("Coco")
print(f"La fruta esta en la posicion: {indice}")
#buscar dato si exite o no
print("Kiwi" in frutas) #true or false
#ordena alfabeticamente
frutas.sort()
print(frutas)
frutasDes = sorted(frutas, reverse =True)
print(frutasDes)
#tamaño de la lista
print(len(frutas))