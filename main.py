import platform
from os import system as term
from time import sleep

if platform.system() == 'Windows':
    termv:str = 'cls'
elif platform.system() == 'Linux':
    termv:str = 'clear'
    
class ems:
    
    def __init__(self):
        pass
    
    @classmethod
    def main(cls):
        menu:str = ("""
========== RRHH EMS ==========
0. Salir
==============================
""")
        
        while True:
            term(termv)
            print(menu)
            input()
            
if __name__ == '__main__':
    ems.main()