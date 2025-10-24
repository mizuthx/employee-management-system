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

    @staticmethod
    def agregar_empleados(c):
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
            #con.desconectar(). no se usa porque ahora se ejecuta al finalizar el def 
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
                print("Conexión (agregar_empleado) cerrada.")

    #de aqui a abajo tengo que actualizar bien completo este crud mañana y los que falten 
    
    
    
    def listar_empleados():
        con = None
        try:
            # usar la conexión local, igual que en CREATE, si quieres cambiar se cambia sin problema 
            con = Conexion(host, user, password, port, db)
            
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
            cursor = con.ejecuta_query(sql)
            
            # Obtenemos todos los resultados del cursor
            resultados = cursor.fetchall()
            
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
            # Si 'ejecuta_query' falla, ya hace rollback.
            return False, f"Error al listar empleados: {e}"
        
        finally:
                #siempre se ejecuta despues del try :3 
            if con:
                con.desconectar()#asegura que no quede la conexion al wamp colgando y cierra si o si, solo si con= true
                print("Conexión (listar_empleados) cerrada.")
    
    @staticmethod
    def buscar_empleado(id_empleado: int):
        con = None 
        try:
            con = Conexion(host, user, password, port, db)
            
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
            
            params = (id_empleado,) 
            
            cursor = con.ejecuta_query(sql, params)
            
            row = cursor.fetchone() 
            
            if row:
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
        
        finally:
            if con:
                con.desconectar()
                print("Conexión (buscar_empleado) cerrada.")

    @staticmethod
    def actualizar(id_empleado: int, empleado: EmpleadoDTO):
        con = None
        try:
            con = Conexion(host, user, password, port, db)
            
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
            
            params = (
                empleado.nombre,
                empleado.primer_apellido,
                empleado.segundo_apellido,
                empleado.numero_tel, 
                empleado.email,
                empleado.inicio_contrato,
                empleado.salario,
                empleado.id_departamento, 
                id_empleado
            )
            
            #Ejecuta query con commit
            cursor = con.ejecuta_query(sql, params, cmt=True)
            
            #Verificamos si realmente se actualizó algo
            if cursor.rowcount > 0:
                return True, "Empleado actualizado exitosamente"
            else:
                return False, "Empleado no encontrado (0 filas actualizadas)"
        
        except mariadb.IntegrityError as e:
            return False, f"Error de integridad: {e}"
        except Exception as e:
            return False, f"Error al actualizar empleado: {e}"
        
        finally:
            if con:
                con.desconectar()
                print("Conexión (actualizar) cerrada.")

    @staticmethod
    def eliminar(id_empleado: int):
        con = None
        try:
            con = Conexion(host, user, password, port, db)
            
            sql = "DELETE FROM empleados WHERE id_empleado = ?"
            
            params = (id_empleado,)
            
            cursor = con.ejecuta_query(sql, params, cmt=True)
            
            # si borra algo avisa 
            if cursor.rowcount > 0:
                return True, "Empleado eliminado exitosamente"
            else:
                return False, "Empleado no encontrado (0 filas eliminadas)"

        except mariadb.IntegrityError as e:
            return False, "No se puede eliminar: el empleado tiene registros asociados (Error de integridad)"
        except Exception as e:
            return False, f"Error al eliminar empleado: {e}"
        
        finally:
            if con:
                con.desconectar()
                print("Conexión (eliminar) cerrada.")

    @staticmethod
    def listar_por_departamento(id_departamento: int):
        con = None
        try:
            con = Conexion(host, user, password, port, db)
            
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
            
            params = (id_departamento,)
            
            cursor = con.ejecuta_query(sql, params)
            
            resultados = cursor.fetchall()
            
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
                    'id_departamento': row[8],
                    'departamento': row[9]
                }
                empleados.append(empleado_info)
            
            return True, empleados
        
        except Exception as e:
            return False, f"Error al listar empleados por departamento: {e}"
        
        finally:
            if con:
                con.desconectar()
                print("Conexión (listar_por_depto) cerrada.")
