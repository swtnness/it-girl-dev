#Hacer un programa que lea la edad de una persona
#y valide si es mayor edad o no

print("="*30)
print("Programa para validar la edad de una persona")
print("="*30)
edad = int(input("Ingrese su edad:\n"))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")