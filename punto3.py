#En un almacén se descuenta el 20% del precio al cliente solo si el valor a pagar supera $200.000.
#Debe mostrar lo que debe pagar el cliente, además del valor del descuento y el valor inicial.

precio_1 = float(input("Ingrese el precio del producto: \n"))
if precio_1 > 200000:
    descuento = precio_1 * 0.20
else:
    descuento = 0
    
total_compra = precio_1 - descuento

print(f"Valor inicial {precio_1}")
print(f"Valor inicial: {precio_1}")
print(f"Valor del descuento: {descuento}")
print(f"Total a pagar: {total_compra}")