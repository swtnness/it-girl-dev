#Calcular el numero de pulsaciones de una persona
#por cada 10 segundos de ejercicio, se debe validar
#genero de la persona para aplicar la formula
#si es masculino n_pulsaciones = (210 - edad)/10
#si es femenino n_pulsaciones = (220 - edad)/10

print("="*50)
print("Programa para calcular el numero de pulsaciones por cada 10 segundos de ejercicio")
print("="*50)
edad = int(input("Ingrese su edad:\n"))
genero = input("Ingrese su genero (M/F): \n").upper()
if genero == "M":
    n_pulsaciones = (210 - edad) / 10
    print(f"El numero de pulsaciones por cada 10 segundos de ejercicio es: {n_pulsaciones:.2F}, genero: {genero}")
elif genero == "F":
    n_pulsaciones = (220 - edad) / 10
    print(f"El numero de pulsaciones por cada 10 segundos de ejercicio es: {n_pulsaciones:.2F}, genero: {genero}")
else:
    print("(┬┬﹏┬┬) Error")