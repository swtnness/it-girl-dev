#En un almacén se rebaja el 10% del precio al cliente si compra más de 20 artículos 
# y 5% si la cantidad de artículos es menor o igual a 20. Luego de ingresar el precio unitario 
# de un artículo y la cantidad adquirida, 
# muestre el valor del descuento y lo que debe pagar el cliente.

precio_unico = float(input("Ingrese el precio de un solo articulo: \n"))
cantidad = int(input("Ingrese la cantidad de articulos: \n"))

subtotal = precio_unico * cantidad

if cantidad > 20:
    descuento = 0.10
else:
    descuento = 0.05
    
porcentaje_descuento = subtotal * descuento
total_pagar = subtotal - porcentaje_descuento

print(f"Subtotal: {subtotal}")
print(f"Total a pagar con descuento: {total_pagar}")