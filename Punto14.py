#Realizar un programa que lea la edad y el género de una persona.
#Si es mayor de edad y es femenino se gana un Bono 
#de 500 mil pesos, de lo contrario No tiene derecho a Bono.

edad = int(input("Ingrese su edad: \n"))
genero = input("Ingrese su género (F/M): \n").upper()

if edad >= 18 and genero == "F":
    print("Felicidades!^_^ Se ha ganado un Bono de $500.000 pesos.")
else:
    print("No tiene derecho a Bono.")