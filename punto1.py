#Hcaer una cuenta regresiva

import time
import os

hora = int(input("Ingrese la hora que desea explotar la bomba: \n"))
minuto = int(input("Ingrese los minutos que desea explotar la bomba: \n"))
segundos = int(input("Ingrese los segundos que desea explotar la bomba: \n"))

for hora in range(hora, -1, -1):
    for minuto in range(minuto, -1, -1):
        for segundos in range(segundos, -1, -1):
            os.system("cls")
            print(f"La bomba explotará en: {hora:02}:{minuto:02}:{segundos:02}")
            time.sleep(1)
