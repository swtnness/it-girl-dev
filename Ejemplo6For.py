#Hacer un programa que lea un numero por consola
#debe imprimir su tabla de multiplicar

numero = int(input("Ingrese un número: \n"))

for i in range(1, 11):
    print(f"{numero} x {i} = {(numero*i)}")