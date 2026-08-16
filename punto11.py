#Elabore un programa en Python que lea tres (3) números y los imprima en forma ascendente

num1 = float(input("Ingrese el primer número: \n"))
num2 = float(input("Ingrese el segundo número: \n"))
num3 = float(input("Ingrese el tercer número: \n"))

if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        menor, medio, mayor = num1, num2, num3
    else:
        menor, medio, mayor = num1, num3, num2
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        menor, medio, mayor = num2, num1, num3
    else:
        menor, medio, mayor = num2, num3, num1
else:
    if num1 <= num2:
        menor, medio, mayor = num3, num1, num2
    else:
        menor, medio, mayor = num3, num2, num1

print("Los números en orden ascendente son:")
print(f"{menor} - {medio} - {mayor}")