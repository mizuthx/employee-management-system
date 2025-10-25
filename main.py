from time import sleep
from src.dto.proyecto import ProyectoDTO
from src.dao.CRUD_proyectos import ProyectoDAO
from src.ui.ems import ems_menu
from src.utils.input_handler import x_input
from src.utils.clear_handler import x_clear
class empleados:
    pass

class departamentos:
    pass

class proyectos:
    
    pass

class ems:
    @classmethod
    def main(cls):
        while True:
            x_clear()
            ems_menu('main')
            x = x_input('str')
            print(x)
            

if __name__ == '__main__':
    ems.main()