#En un estacionamiento de motos cobran $ 1.500 por hora o fracción. 
#Diseñe un algoritmo que determine cuanto debe pagar un cliente
#por el estacionamiento de su vehículo, conociendo el tiempo de estacionamiento en minutos.

MINUTOS = int(input("Ingrese el tiempo en estacionamiento en minutos: \n"))

TARIFA_HORA = 1500

hora_completa = MINUTOS // 60
minutos_sobran = MINUTOS % 60

if minutos_sobran > 0:
    hora_acobrar = hora_completa + 1
else:
    hora_acobrar = hora_completa
    
total_pagar = hora_acobrar * TARIFA_HORA

print(f"Tiempo completado: {MINUTOS}")
print(f"Hora/minutos cobrados: {hora_acobrar}")
print(f"Total a pagar: {total_pagar}")