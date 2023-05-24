import numpy as np
import pandas as pd
import pickle
import serial
from time import sleep
from colorama import init
from colorama.ansi import Fore

init(autoreset=True)

colores = ['Rojo', 'Verde', 'Azul', 'Amarillo'] 
fores = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW]

model = pickle.load(open('SVC.sav', 'rb'))

uno = serial.Serial('/dev/ttyACM0', 9600)
sleep(2)

while True:
    try:
        data = str(uno.readline(), encoding='utf-8')
        data = data.replace('\r\n', '')
        data = [int(i) for i in data.split('-')]

        r, g, b, = data
        print(Fore.RED + f"R={r}\t" + Fore.GREEN + f"G={g}\t" + Fore.BLUE + f"B={b}", end='')

        x = np.array([[r, g, b]])
        y = model.predict(x)[0]
        print(fores[y] + f"\t==> [***] {colores[y]}")

    except Exception as e:
        print(Fore.YELLOW + "[!] Excepcion:")
        print(e)
        break

uno.close()
print(Fore.YELLOW + "[!] Conexion terminada")

