#Crear un programa que solicite notas al usuario de forma indefinida y calcule el promedio. El  
#programa debe finalizar cuando el usuario ingrese una nota negativa, utilizando un ciclo while.

suma_notas = 0
contador = 0

nota = float(input("Ingrese una nota (o un número negativo para salir): \n"))

while nota >= 0:
    suma_notas += nota
    contador += 1
    nota = float(input("Ingrese otra nota (o un número negativo para salir): \n"))

if contador > 0:
    promedio = suma_notas / contador
    print(f"Cantidad de notas ingresadas: {contador}")
    print(f"El promedio final es: {promedio}")
else:
    print("Ingrese notas validasಥ_ಥ.")