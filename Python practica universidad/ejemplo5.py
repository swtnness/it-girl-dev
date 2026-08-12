#Hacer un programa que lea un numero y valide si es un numero par o impar
print("="*50)
print("Programa para validar si un numero es par o impar")
print("="*50)
numero = int(input("Ingrese un numero:\n"))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")