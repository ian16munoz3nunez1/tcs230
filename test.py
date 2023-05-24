import cv2 as cv
import numpy as np
import pandas as pd
import pickle
import serial
from time import sleep
from colorama import init
from colorama.ansi import Fore, Back, Style

init(autoreset=True)

fondos = [(255, 82, 82), (82, 255, 84), (82, 82, 255), (255, 255, 82), (255, 82, 255), (255, 148, 82), (191, 191, 191), (64, 64, 64)]
colores = ['Rojo', 'Verde', 'Azul', 'Amarillo', 'Morado', 'Naranja', 'Blanco', 'Negro']

fores = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.YELLOW, Fore.WHITE, Fore.BLACK]
backs = [Back.BLACK, Back.BLACK, Back.BLACK, Back.BLACK, Back.BLACK, Back.BLACK, Back.BLACK, Back.WHITE]
style = [Style.BRIGHT, Style.BRIGHT, Style.BRIGHT, Style.BRIGHT, Style.BRIGHT, Style.DIM, Style.BRIGHT, Style.BRIGHT, Style.NORMAL]

imagen = np.zeros((500, 500, 3), dtype=np.uint8)
cv.namedWindow('TCS230', cv.WINDOW_NORMAL)

model = pickle.load(open('SVC.sav', 'rb'))

uno = serial.Serial('/dev/ttyACM0', 9600)
sleep(2)
print(Fore.GREEN + "[+] Conexion establecida")

while True:
    try:
        data = str(uno.readline(), encoding='utf-8')
        data = data.replace('\r\n', '')
        data = [int(i) for i in data.split('-')]

        r, g, b, = data
        print(Fore.RED + f"R={r}\t" + Fore.GREEN + f"G={g}\t" + Fore.BLUE + f"B={b}", end='')

        x = np.array([[r, g, b]])
        y = model.predict(x)[0]
        print(style[y] + backs[y] + fores[y] + f"\t==> [***] {colores[y]}")

        imagen[:, :, 2] = fondos[y][0]
        imagen[:, :, 1] = fondos[y][1]
        imagen[:, :, 0] = fondos[y][2]
        cv.imshow('TCS230', imagen)
        if cv.waitKey(1) == 27:
            break

    except Exception as e:
        print(Fore.YELLOW + "[!] Excepcion:")
        print(e)
        break

uno.close()
cv.destroyAllWindows()
print(Fore.YELLOW + "[!] Conexion terminada")

