import platform
from os import system as term
from time import sleep
from src.dao.database import db
# import class DTO / DAO ?

if platform.system() == 'Windows':
    termv:str = 'cls'
elif platform.system() == 'Linux':
    termv:str = 'clear'
    
class ems:
    @classmethod
    def x_input(cls, name:str = 'Opcion', tipo:bool = False):
        if tipo == False:
            try:
                tmp = int(input(name + ': '))
                return tmp
            except ValueError as e:
                term(termv)
                print(f"Entrada no valida\n\n{e}")
                sleep(2)
                return None
        elif tipo == True:
            try:
                tmp = str(input(name + ': '))
                return tmp
            except ValueError as e:
                term(termv)
                print(f"Entrada no validan\n\n{e}")
                sleep(2)
                return None
    
    @classmethod
    def proyectos(cls):
        menu:str = ("""
========== Proyectos ==========
1.  Listar
2.  Agregar
3   Editar
4.  Eliminar
0.  Volver
===============================
""")
        term(termv)
        while True:
            term(termv)
            print(menu)
            x = cls.x_input()
            if x == 1:
                pass
            elif x == 2:
                pass
            elif x == 3:
                pass
            elif x == 0:
                break
    
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
            x = cls.x_input()
            if x == 1:
                pass
            elif x == 2:
                pass
            elif x == 3:
                pass
            elif x == 4:
                pass
            elif x == 0:
                break
    
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
            elif x == 2:
                pass
            elif x == 3:
                cls.proyectos()
            elif x == 0:
                break
    @staticmethod
    def check():
        if db.model_chx() == False:
            term(termv)
            print("\n\n\nDB -- > Modelo Inexistente, Creando")
            sleep(0.5)
            ems.main()
        elif db.model_chx() == True:
            term(termv)
            print("\n\n\nDB --> Modelo existente, Omitiendo")
            sleep(0.5)
            ems.main()
        else:
            term(termv)
            print(f"""\n\n
DB --> Se ha producido un error al intentar crear el modelo\n
{db.model_chx()}
""")
            input('Presione ENTER para continuar...')
            
if __name__ == '__main__':
    ems.check()