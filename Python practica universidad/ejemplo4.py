#Hacer un programa que lea un numero y evalua si es positivo, negativo o neutro
print("="*50)
print("Programa para validar si un numero es positivo, negativo o neutro")
print("="*50)
numero = int(input("Ingrese un numero:\n"))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es neutro")
