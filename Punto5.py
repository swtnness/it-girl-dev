#En un almacén se hace un 20% de descuento a los clientes 
# cuya compra supere los $100.000 ¿Cuál será la cantidad que pagara una persona por su compra?

compra = float(input("Ingrese el valor total de su compra: \n"))

if compra > 100000:
    descuento = compra * 0.20
    total = compra - descuento
    print(f"Se aplicó un 20% de descuento en su compra, el valor total es: {total}")
    
else:
    total = compra
    print(f"El valor total de su compra es: {total}")