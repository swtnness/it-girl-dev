#Hcaer un programa que lea una clave de usuario y valide si es incorrecta
#y vuelva a solicitar la contraseña, y si es correcta panel de bienvenida

CLAVE = "jorgeelcurioso"
USUARIO = "Vannecita"

intentos = 0

contraseña = input("Ingrese su contraseña de acceso: \n")
usuario = input("Ingrese su nombre de usuario: \n")

while (contraseña != CLAVE or usuario != USUARIO) and intentos <3:
    intentos +=1
    print("Error: usuario o contraseña son incorrectos")
    contraseña = input("Ingrese nuevamente la contraseña: \n")
    usuario = input("Ingrese nuevamente el usuario: \n")

if usuario == USUARIO and contraseña  == CLAVE:
    print("Bienvenido(❁´◡`❁)")
    
else:
    print("Usuario bloqueado, vuelva intentar en una hora")
    
