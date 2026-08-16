#Hacer un progama que imprima el nombre de un artículo, categoría, precio original y 
# su precio con descuento. El descuento lo hace en base a la categoría, si es A el descuento es del 10%
# y si la categoría es B el descuento es del 20% (solo existen dos claves).

nombre = input("Ingrese el nombre del articulo: \n")
categoria = input("Ingrese que categoria es el articulo (A/B): \n").upper()
precio_original = float(input("Ingrese el precio del articulo: \n"))

if categoria == "A":
    descuento = precio_original * 0.10
elif categoria == "B":
    descuento = precio_original * 0.20
else:
    descuento = 0
    print("Error: este articulo no tiene descuento")

totalfinal = precio_original - descuento

print("Resumen de la compra")
print(f"Articulo {nombre}")
print(f"Categoria: {categoria}")
print(f"El valor original del articulo es {precio_original}")
print(f"El descuento aplicado es de: {totalfinal}")
