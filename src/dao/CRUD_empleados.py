#from database import db -no se usa en el archivo
#from .database import db -repetido
from dao.Conexion import Conexion
from ..dto.empleado import EmpleadoDTO
import mariadb

host = 'localhost'
user = 'root'
password = ''
port = 3307
db = 'gestion_empleados'
#CRUD = CREATE, READ, UPDATE, DELETE
class EmpleadoDAO:
    
    def CREATE(c):
        con = None
        try:
            con = Conexion(host, user, password, port, db)
            sql = """
            INSERT INTO empleados 
            (nombre, primer_apellido, segundo_apellido, telefono, email, inicio_contrato, salario, id_departamento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            params = (c.nombre, 
                c.primer_apellido, 
                c.segundo_apellido, 
                c.telefono, 
                c.email, 
                c.inicio_contrato, 
                c.salario, 
                c.id_departamento,
            )
            con.ejecuta_query(sql,params,cmt=True)
            #con.commit(). no se usa porque lo hace el ejecuta_query
            print("Datos ingresadooos!!!")
            con.desconectar()
        except mariadb.IntegrityError as e:
            #con.rollback no se usa porque ahora lo tiene ejecuta_query
            print(f'no se pudo {e}')
        except Exception as e:
            #con.rollback() de nuevo lo mismo que el anterior
            print(f'no se pudo{e}')
        finally:
            #finally se ejecuta si o si despues de un try 
            if con:   #if con: si con es True = se desconecta y printea que se cierra la conexion para ahorrar datos"
                con.desconectar()
                print("Conexión cerrada.")

    #de aqui a abajo tengo que actualizar bien completo este crud mañana y los que falten 
    
    @staticmethod
    #listar a los empleados
    def listar():
        try:
            sql = """
            SELECT 
                e.id_empleado,
                e.nombre,
                e.primer_apellido,
                e.segundo_apellido,
                e.telefono,
                e.email,
                e.inicio_contrato,
                e.salario,
                d.nombre as departamento
            FROM empleados e
            INNER JOIN departamentos d ON e.id_departamento = d.id_departamento
            ORDER BY e.id_empleado
            """
            resultados = db.query(sql, row=None)
            
            empleados = []
            for row in resultados:
                empleado_info = {
                    'id': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3] or '', 
                    'telefono': row[4],
                    'email': row[5],
                    'inicio_contrato': row[6],
                    'salario': row[7],
                    'departamento': row[8]
                }
                empleados.append(empleado_info)
            
            return True, empleados
        except Exception as e:
            return False, f"Error al listar empleados: {e}"
    
    @staticmethod
    def buscar(id_empleado:int):
        try:
            sql = """
            SELECT 
                e.id_empleado,
                e.nombre,
                e.primer_apellido,
                e.segundo_apellido,
                e.telefono,
                e.email,
                e.inicio_contrato,
                e.salario,
                e.id_departamento,
                d.nombre as departamento
            FROM empleados e
            INNER JOIN departamentos d ON e.id_departamento = d.id_departamento
            WHERE e.id_empleado = ?
            """
            resultado = db.query(sql, (id_empleado,), row=1)
            
            if resultado and len(resultado) > 0:
                row = resultado[0]
                empleado_info = {
                    'id': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3] or '',
                    'telefono': row[4],
                    'email': row[5],
                    'inicio_contrato': row[6],
                    'salario': row[7],
                    'id_departamento': row[8],
                    'departamento': row[9]
                }
                return True, empleado_info
            else:
                return False, "Empleado no encontrado"
        except Exception as e:
            return False, f"Error al buscar empleado: {e}"
    
    @staticmethod
    def actualizar(id_empleado:int, empleado:EmpleadoDTO, id_departamento:int):
        try:
            existe, _ = EmpleadoDAO.buscar(id_empleado) #VERIFICACIOON!!!
            if not existe:
                return False, "Empleado no encontrado"
            
            sql = """
            UPDATE empleados 
            SET nombre = ?, 
                primer_apellido = ?, 
                segundo_apellido = ?,
                telefono = ?, 
                email = ?, 
                inicio_contrato = ?, 
                salario = ?,
                id_departamento = ?
            WHERE id_empleado = ?
            """
            
            
            data = (
                empleado.nombre,
                empleado.primer_apellido,
                empleado.segundo_apellido,
                str(empleado.numero_tel),
                empleado.email,
                empleado.inicio_contrato,
                empleado.salario,
                id_departamento,
                id_empleado
            )
            
            db.query(sql, data, cmt=True)
            return True, "Empleado actualizado exitosamente"
        except mariadb.IntegrityError as e:
            db.rollback()
            return False, f"Error de integridad: {e}"
        except Exception as e:
            db.rollback()
            return False, f"Error al actualizar empleado: {e}"
    
    @staticmethod
    def eliminar(id_empleado: int):
        try:
            existe, _ = EmpleadoDAO.buscar(id_empleado)
            if not existe:
                return False, "Empleado no encontrado"
            
            sql = "DELETE FROM empleados WHERE id_empleado = ?"
            db.query(sql, (id_empleado,), cmt=True)
            return True, "Empleado eliminado exitosamente"
        except mariadb.IntegrityError as e:
            db.rollback()
            return False, "No se puede eliminar: el empleado tiene registros o proyectos asociados"
        except Exception as e:
            db.rollback()
            return False, f"Error al eliminar empleado: {e}"
    
    @staticmethod
    def listar_por_departamento(id_departamento: int):
        """
        Lista todos los empleados de un departamento específico
        """
        try:
            sql = """
            SELECT 
                e.id_empleado,
                e.nombre,
                e.primer_apellido,
                e.segundo_apellido,
                e.telefono,
                e.email,
                e.salario
            FROM empleados e
            WHERE e.id_departamento = ?
            ORDER BY e.nombre, e.primer_apellido
            """
            resultados = db.query(sql, (id_departamento,), row=None)
            
            empleados = []
            for row in resultados:
                empleado_info = {
                    'id': row[0],
                    'nombre': f"{row[1]} {row[2]} {row[3] or ''}".strip(),
                    'telefono': row[4],
                    'email': row[5],
                    'salario': row[6]
                }
                empleados.append(empleado_info)
            
            return True, empleados
        except Exception as e:
            return False, f"Error al listar empleados por departamento: {e}"