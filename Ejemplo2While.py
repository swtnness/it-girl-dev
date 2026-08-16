#Hacer un programa que lea un numero y valide si es positivo de lo contrario
#debe de solicitar nuevamente un numero hasta que el número sea correcto

numero = int(input("Ingrese un número: \n"))

while numero<0:
    print("Ingrese un número valido")
    numero = int(input("Ingrese un número: \n"))
    
print(f"El número ingresado es correcto {numero}")