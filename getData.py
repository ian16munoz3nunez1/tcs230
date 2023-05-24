import serial
from time import sleep
from colorama import init
from colorama.ansi import Fore

init(autoreset=True)

colores = ['Rojo', 'Verde', 'Azul', 'Amarillo']

uno = serial.Serial("/dev/ttyACM0", 9600)
sleep(2)

archivo = open("color.csv", 'w')
# archivo = open("color.csv", 'a+')
archivo.write("name,r,g,b,color\n")

i = 0
while i < 100:
    try:
        data = str(uno.readline(), encoding='utf-8')
        data = data.replace('\r\n', '')
        data = data.split('-')

        r, g, b = data
        print(r, g, b, "<==>", i+1)
        archivo.write(f"{colores[0]},{r},{g},{b},0\n")

        i += 1

    except Exception as e:
        print(e)
        break

uno.close()
print(Fore.YELLOW + "[!] Conexion terminada")
archivo.close()

