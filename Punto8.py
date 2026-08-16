#La empresa X-Terminion, hace partícipes a sus colaboradores de las utilizadas de la empresa.
#Calcular la utilidad que un trabajador recibe dependiendo de su
#antigüedad en la empresa de acuerdo con la siguiente tabla:

salario = float(input("Ingrese el salario del trabajador: \n"))
antiguedad = float(input("Ingrese la antiguedad del trabajador: \n"))

if antiguedad <= 1:
    porcentaje = 0.05
elif antiguedad < 3:
    porcentaje = 0.07
elif antiguedad < 5:
    porcentaje = 0.10
elif antiguedad < 10:
    porcentaje = 0.15
else:
    porcentaje = 0.20
    
utilidad = salario * porcentaje
total_salario = salario + utilidad

print("Resumen de utilidad del trabajador")
print(f"Salario base {salario}")
print(f"Antiguedad del trabajador {antiguedad}")
print(f"Total de recibir {total_salario}")
    