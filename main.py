import platform
from os import system as term
from time import sleep

# import class DTO / DAO ?

if platform.system() == 'Windows':
    termv:str = 'cls'
elif platform.system() == 'Linux':
    termv:str = 'clear'
    
class ems:
    
    # INPUT FUNCTION
    @classmethod
    def x_input(cls, name:str = 'Opcion', tipo:bool = False):
        if tipo == False:
            try:
                tmp = int(input(name + ': '))
                return tmp
            except ValueError as e:
                print(f"Entrada no valida \nERROR --> {e}")
                sleep(2)
                return None
        elif tipo == True:
            try:
                tmp = str(input(name + ': '))
                return tmp
            except ValueError as e:
                print(f"Entrada no valida \nERROR --> {e}")
                sleep(2)
                return None
    
    @classmethod
    def empleados(cls):
        menu:str = ("""
========== Empleados ==========
1. Listar
2. Agregar 
3. Editar
4. Eliminar
0. Volver
===============================
""")
        while True:
            term(termv)
            print(menu)
            input()
    
    @classmethod
    def main(cls):
        menu:str = ("""
========== RRHH EMS ==========
1. Empleados
2. Departamentos
3. Proyectos
0. Salir
==============================
""")
        
        while True:
            term(termv)
            print(menu)
            x = cls.x_input()
            if x == 1:
                cls.empleados()
            elif x == 0:
                break
            
            
if __name__ == '__main__': #when the file is running exec ts below
    ems.main()