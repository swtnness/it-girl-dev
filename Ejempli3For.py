#Hacer un programa que imprima la siguiente frecuenta
#con un ciclo for
#0-11-22-33-44-55...99

for i in range(0, 100, 11):
    print(f"{i}", end="-")
    
print(" ")
#0-0-5-3-10-6-15-9-20-12
secuencia = 0
for i in range(0, 21, 5):
    print(f"{i}-{secuencia}", end= " ")
    secuencia +=3
    
    
    