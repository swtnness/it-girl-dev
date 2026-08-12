#Hacer un programa que lea un numero
#y valide si es mayor a 10 y debe de entregar la mitad del mismo
#de lo contrario debe de entregar el doble del mismo

print("="*50)
print("Programa para validar un numero y entregar su mitad o el doble")
print("="*50)
numero = int(input("Ingrese un numero:\n"))
if numero > 10:
    print("El numero es mayor a 10, la mitad de su valor es:", numero / 2)
else:
    print("El numero es menor o igual a 10, el doble de su valor es:", numero *2)