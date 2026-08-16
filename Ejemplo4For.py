#Hahcer un programa que lea el numero en consola
#y valide con un ciclo si es numero primo o no es

numero = int(input("Ingrese un número: \n")) 
cont = 0
for i in range(1, numero+1):
    if numero % i == 0:
        cont += 1
        
if cont == 2:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} no es primo")