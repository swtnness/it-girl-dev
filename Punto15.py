#Diseñar un programa que solicite un número al usuario 
#y muestre su tabla de multiplicar del 1 al 10 utilizando
#un ciclo for.

numero = int(input("Ingrese el número para ver la tabla de multiplicar: \n"))

print(f"--- TABLA DEL {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")