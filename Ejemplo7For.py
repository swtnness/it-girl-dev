#Hacer un programa que imprima las 10 tablas de multiplicacion

for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {(i*j)}")
    print(" ")