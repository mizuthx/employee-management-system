import platform
from os import system

def x_clear():
    if platform.system() == 'Windows':
        system('cls')
    elif platform.system() == 'Linux':
        system('clear')
    else:
        print('No se pudo detectar la plataforma...')