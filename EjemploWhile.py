#Hacer un programa que genere un cronograma,
#debe mostrar la hora, los minutos y segundos

import time
import os

for horas in range(0, 24):
    for minutos in range(0, 60):
        for segundo in range(0, 60):
            os.system("cls")
            print(f"{horas:02}:{minutos:02}:{segundo:02}")
            time.sleep(0.001)