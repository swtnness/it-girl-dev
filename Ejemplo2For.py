#Hacer un programa que sume los primeros 100 numeros enteros por medio
#de un ciclo FOR, debe imprimir la suma total.

suma = 0
for i in range(1, 101):
    suma += i
print(f"La suma de los 100 primeros números es: {suma}")

"""Hacer un programa que sume los primeros 200 numeros pares en un ciclo"""

suma2 = 0
for i in range(0, 401, 2):
    suma2 += i
print(f"La suma de los 200 primeros numeros pares es: {suma2}")
