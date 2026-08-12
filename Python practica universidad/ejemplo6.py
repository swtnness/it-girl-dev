#Hacer un programa que emplea 3 notas de un estudiante debe calcular el promedio
#de la nota y entregar la evaluacion, con las siguientes condiciones:
#1. Si la nota es de 0 a menor de 2 pierde el modulo
#2. Si la nota es de 2 a menor a 3 habilita el modulo
#3. Si la nota es de 3 en adelante aprueba el modulo

print("="*50)
print("Programa para calcular el promedio de 3 notas")
print("="*50)

nota1 = float(input("Ingrese la primera nota:\n"))
nota2 = float(input("Ingrese la segunda nota:\n"))
nota3 = float(input("Ingrese la tercera nota:\n"))

promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 3:
    print(f"El promedio es: {promedio}, Aprueba el modulo")

elif promedio < 2:
    print(f"El promedio es: {promedio}, Pierde el modulo")

else:
    print(f"El promedio es: {promedio}, Habilite el modulo")