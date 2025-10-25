menu:dict = {
    'main': """
========== Gestor de Empleados ========== 
1. Empleados
2. Departamentos
3. Proyectos
0. Salir
=========================================
    """,
    'empleados': """
========== Empleados ========== 
1. Listar
2. Agregar
3. Editar
4. Eliminar
0. Volver
===============================
""",
    'Departamentos': """
========== Departamentos ==========
1. Listar
2. Agregar
3. Editar
4. Eliminar
0. Volver
===================================
""",
    'proyectos': """
========== Proytectos ==========
1. Listar
2. Agregar
3. Editar
4. Eliminar
0. Volver
================================    
"""
}

def ems_menu(tipo:str):
    if tipo in menu:
        print(menu[tipo])
    else:
        print('MENU NO ENCONTRADO...')
if __name__ == '__main__':
    ems_menu('main')