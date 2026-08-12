#Hacer un programa que lea el total de la compra
#si la compra es mayor 1200000, se le aplica un descuento del 15%
#de lo contrario se aplica el 4.5%, debe imprimir el valor de la compra, el descuento y el total a pagar

print("="*50)
print("Programa para calcular el total de la compra")
print("="*50)

total_compra =float(input("Ingrese el total de la compra:\n"))
if total_compra > 1200000:
    descuento = total_compra * 0.15
    print(f"El valor de la compra es {total_compra}, el descuento es {descuento} y el total a pagar es {total_compra - descuento}")
else:
    descuento = total_compra * 0.045
    print(f"El valor de la compra es {total_compra}, el descuento es {descuento} y el total a pagar es {total_compra - descuento}")