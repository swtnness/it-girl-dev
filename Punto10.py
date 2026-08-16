#Crear un programa que solicite al usuario un número entero positivo y 
#calcule la suma de todos los números desde 1 hasta ese número usando un ciclo for 

numero = int(input("Ingrese un numero positivo valido: \n"))

if numero > 0:
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    print(f"La suma de los números del 1 al {numero} es {suma}")  
else:
    print("El numero debe ser mayor a 0")
