from dao.Conexion import Conexion
from ..dto.departamento import DepartamentoDTO
import mariadb
from .database import db

host = 'localhost'
user = 'root'
password = ''
port = 3307
db = 'gestion_empleados'

class DepartamentoDAO(DepartamentoDTO):
    def __init__(self, nombre, descripcion ,id_empleado):
        super().__init__(nombre, descripcion,id_empleado)

    @classmethod
    def agregar_departamento(cls, d):
            tmp = db.query('INSERT INTO Departamentos (nombre, descripcion ,id_usuario) VALUES (?, ? , ?)', 
                           d.nombre, d.descripcion ,d.id_empleado,
                           cmt=True)
            print(tmp)
            input()
    
    @classmethod
    def eliminar_departamento(cls, d):
         tmp = db.query('DELETE FROM Departamentos where id_departamento = ?;',
                        d.id_departamento,
                        cmt=True)
         print(tmp)
         input()
    
    @classmethod
    def actualizar_departamento(cls, d):
         tmp = db.query('UPDATE Departamentos set (nombre, descipcion, id_usuario) VALUES (?,?,?);',
                        d.nombre, d.descripcion, d.id_empelado,
                        cmt=True)
         print(tmp)
         input()

    @classmethod
    def listar_departamento(cls, d):
         tmp = db.query('SELECT * FROM departamentos')
         print(tmp)
         input()