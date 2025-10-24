from .database import db
from datetime import date
from ..dto.proyecto import ProyectoDTO

class ProyectoDAO(ProyectoDTO):
    def __init__(self, nombre, descripcion, fecha_inicio):
        super().__init__(nombre, descripcion, fecha_inicio)
        
    def __str__(self):
        return super().__str__(self.nombre)
    
    @classmethod
    def agregar(cls, p):
        tmp = db.query('INSERT INTO proyectos (id_empleado, nombre, descripcion, fecha_inicio) VALUES (?, ?, ?, ?)',
                 (0, p.nombre, p.descripcion, date(p.fecha_inicio[2],p.fecha_inicio[1],p.fecha_inicio[0])), cmt= True)
        return tmp