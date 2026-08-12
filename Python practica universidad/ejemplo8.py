dia = int(input("Ingrese el dia de nacimiento: \n"))
mes = input("Ingrese el mes de nacimiento: \n").strip().lower()

if (dia>=21 and dia <=31 and mes == "marzo") or (dia >=1 and dia <=19 and mes == "abril"):
    print("Su signo zodiacal es Aries")
elif (dia>=20 and dia <=20 and mes == "abril") or (dia >=1 and dia <=20 and mes == "mayo"):
    print("Su signo zodiacal es Tauro")
elif (dia>=21 and dia <=31 and mes == "mayo") or (dia >=1 and dia <=20 and mes == "junio"):
    print("Su signo zodiacal es Geminis")
elif (dia>=21 and dia <=30 and mes == "junio") or (dia >=1 and dia <=22 and mes == "julio"):
    print("Su signo zodiacal es Cancer")
elif (dia>=23 and dia >=31 and mes == "julio") or (dia >=1 and dia <=22 and mes == "agosto"):
    print("Su signo zodiacal es Leo")
elif (dia>=23 and dia <=31 and mes == "agosto") or (dia >=1 and dia <=22 and mes == "septiembre"):
    print("Su signo zodiacal es Virgo") 
elif (dia>=23 and dia <=30 and mes == "septiembre") or (dia >=1 and dia <=22 and mes == "octubre"):
    print("Su signo zodiacal es Libra")
elif (dia>=23 and dia <=31 and mes == "octubre") or (dia >=1 and dia <=21 and mes == "noviembre"):
    print("Su signo zodiacal es Escorpio")
elif (dia>=23 and dia <=30 and mes == "noviembre") or (dia >=1 and dia <=21 and mes == "diciembre"):
    print("Su signo zodiacal es Sagitario")
elif (dia>=22 and dia <=31 and mes == "diciembre") or (dia >=1 and dia <=19 and mes == "enero"):
    print("Su signo zodiacal es Capricornio")
elif (dia>=20 and dia <=28 and mes == "enero") or (dia >=1 and dia <=18 and mes == "febrero"):
    print("Su signo zodiacal es Acuario")
elif (dia>=19 and dia <=29 and mes == "febrero") or (dia >=1 and dia <=20 and mes == "marzo"):
    print("Su signo zodiacal es Piscis")
else:
    print("Error, asigne una fecha correcta O_O")