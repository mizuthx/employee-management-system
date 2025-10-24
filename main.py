import platform
from os import system as term
from time import sleep
from src.dto.proyecto import ProyectoDTO
from src.dao.CRUD_proyectos import ProyectoDAO

# Detecta la plataforma parar ejecutar cls o clear,
# esto por que estudio en distintos entornos
if platform.system() == 'Windows':
    termv:str = 'cls'
elif platform.system() == 'Linux':
    termv:str = 'clear'

class proyectos:
    @classmethod
    def agregar(cls):
        nombre:str = '?'
        descripcion:str = '?'
        fecha_inicio:list = ['DD', 'MM', 'AAAA']

        while True:
            term(termv)
            for i in range(0,7):
                if i == 1:
                    term(termv)
                    print(menu)
                    nombre = ems.x_input('Nombre', 1)
                elif i == 2:
                    term(termv)
                    print(menu)
                    descripcion = ems.x_input('Descripcion', 1)
                elif i == 3:
                    term(termv)
                    print(menu)
                    fecha_inicio[0] = ems.x_input('Dia')
                elif i == 4:
                    term(termv)
                    print(menu)
                    fecha_inicio[1] = ems.x_input('Mes')
                elif i == 5:
                    term(termv)
                    print(menu)
                    fecha_inicio[2] = ems.x_input('Año')
                elif i == 6:
                    term(termv)
                    print(menu)
                    x = ems.x_input('Confirmar datos? (sS/nN)', 2).lower()
                    if x == 's':
                        p = ProyectoDTO(nombre, descripcion, fecha_inicio)
                        ProyectoDAO.agregar(p)
                        break
            
                menu:str = (f"""
========== Agregar Proyecto ==========
Nombre: {nombre}
Descripcion: {descripcion}
Fecha: {fecha_inicio[0]} / {fecha_inicio[1]} / {fecha_inicio[2]}
======================================                   
""")
            break
    
class ems:
    @staticmethod
    def x_input(name:str = 'Opcion', tipo:int = None):
        """
            x_input() default return INT()\n
            tipo = None: INT\n
            tipo = 1: STRING\n
            tipo = 2: sS/nN\n
        """
        i = True
        if tipo == None:
            try:
                tmp = int(input(name + ': '))
                return tmp
            except ValueError as e:
                term(termv)
                print(f"Entrada no valida\n\n{e}")
                sleep(2)
                return None
        elif tipo != None and tipo == 1:
            try:
                tmp = str(input(name + ': '))
                return tmp
            except ValueError as e:
                term(termv)
                print(f"Entrada no valida\n\n{e}")
                sleep(2)
                return None
        elif tipo != None and tipo == 2:
            while i:
                term(termv)
                tmp = str(input(name + ': '))
                if tmp in ('s', 'S', 'n', 'N'):
                    i = False
                    return tmp
                else:
                    term(termv)
                    print("Entrada no valida...")
                    sleep(1)
                
                
            
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
                proyectos.agregar()
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
            
if __name__ == '__main__':
    ems.main()