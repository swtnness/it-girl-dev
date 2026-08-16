#Crear un programa que solicite al usuario una contraseña y continúe pidiéndola  
#mientras sea incorrecta, utilizando un ciclo while.

CLAVE = "jorgetqm"

clave = input("Ingrese la contraseña de usuario: \n")
while clave != CLAVE:
    print("Contraseña incorrecta, intente de nuevo(┬┬﹏┬┬)")
    clave = input("Ingrese de nuevo la contraseña: \n")
    
print("Bienvenido(❁´◡`❁)")                                            