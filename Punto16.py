#Crear un programa que solicite al usuario 5 notas, 
#las almacene y calcule el promedio final utilizando un ciclo for.

notas = []

for i in range(1, 6):
    nota = float(input(f"Ingrese la nota {i}: \n"))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("--- RESUMEN DE NOTAS ---")
print(f"Notas ingresadas: {notas}")
print(f"Promedio final: {promedio}")