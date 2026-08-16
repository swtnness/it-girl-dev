#Diseñar un programa que permita ingresar números y los vaya sumando.
#El programa debe finalizar cuando el usuario ingrese 
#el número 0, utilizando un ciclo while.

suma_total = 0

numero = float(input("Ingrese un número: (0 para terminar): \n"))

while numero != 0:
    suma_total += numero
    numero = float(input("Ingrese otro número (0 para terminar): \n"))

print(f"El resultado total de la suma es: {suma_total}")