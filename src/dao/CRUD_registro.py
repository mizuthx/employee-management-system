from .database import db
from datetime import date
from ..dto.registro import RegistroDTO

class RegistroDAO(RegistroDTO):
    def __init__(self, fecha_inicio, horas, descripcion, id_empleado):
        super().__init__(fecha_inicio, horas, descripcion, id_empleado)
        
    def __str__(self):
        return super().__str__(self.descripcion)
    
@classmethod
def agregar_registro(cls, r):
    tmp = db.query('INSER INTO proyectos (fecha_inicio, horas, descripcion, id_empleado) VALUES (? ,? , ?, ?);',
                   r.fecha_inicio, r.horas, r.descripcion, r.id_empleado,
                   cmt = True)
    print(tmp)
    input()

@classmethod
def eliminar_registro(cls, r):
    tmp = db.query('DELETE FROM registros where id_registro = ?;',
                   r.id_registro,
                   cmt = True)
    print(tmp)
    input()

@classmethod
def actualizar_registro(cls, r):
    tmp = db.query('UPDATE registros set (fecha_inicio, horas, descripcion, id_empleado) VALUES (?, ?, ?, ?);',
                   r.fecha_inicio, r.horas, r.descripcion, r.id_empleado,
                   cmt = True)
    print(tmp)
    input()

@classmethod
def listar_registro(cls, r):
    tmp = db.query('SELECT * FROM registros')
    print(tmp)
    input()