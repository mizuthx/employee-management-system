from .database import db
from datetime import date
from ..dto.empleado import EmpleadoDTO

class EmpleadoDAO:
    @classmethod
    def agregar_empleados(cls, c):
        db.query(
            """
            INSERT INTO empleados 
            (nombre, primer_apellido, segundo_apellido, telefono, email, inicio_contrato, salario, id_departamento)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (c.nombre, 
                c.primer_apellido, 
                c.segundo_apellido, 
                c.telefono,
                c.email, 
                c.inicio_contrato, 
                c.salario, 
                c.id_departamento), 
            cmt= True)
        
    @classmethod
    def listar_empleados(cls):
            resultados = db.query("""
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
            ORDER BY e.id_empleado;""")
            
            empleados = []
            for tmp in resultados:
                empleado_info = {
                    'id': tmp[0],
                    'nombre': tmp[1],
                    'primer_apellido': tmp[2],
                    'segundo_apellido': tmp[3] or '', 
                    'telefono': tmp[4],
                    'email': tmp[5],
                    'inicio_contrato': tmp[6],
                    'salario': tmp[7],
                    'departamento': tmp[8]
                }
                empleados.append(empleado_info)
            return True, empleados
    
    @classmethod
    def buscar_empleado(id_empleado: int):
            tmp = db.query("""
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
            """, (id_empleado,), tmp= 1)
            
            if tmp:
                empleado_info = {
                    'id': tmp[0],
                    'nombre': tmp[1],
                    'primer_apellido': tmp[2],
                    'segundo_apellido': tmp[3] or '',
                    'telefono': tmp[4],
                    'email': tmp[5],
                    'inicio_contrato': tmp[6],
                    'salario': tmp[7],
                    'id_departamento': tmp[8],
                    'departamento': tmp[9]
                }

    @classmethod
    def actualizar(cls, e):
            try:
                fecha_contrato = date(e.inicio_contrato[2], e.inicio_contrato[1], e.inicio_contrato[0])
            except ValueError:
                print('Longitud Fuera de rango...')

            db.query("""
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
            """,
            (e.nombre, e.primer_apellido, e.segundo_apellido, e.numero_tel, fecha_contrato, e.salario, e.id_departamento), cmt= True)

    @classmethod
    def eliminar(cls, e):
        
        db.query("DELETE FROM empleados WHERE id_empleado = ?", (e.id_empelado,))
        con = None
        try:
            con = Conexion(host, user, password, port, db)
            
            sql = "DELETE FROM empleados WHERE id_empleado = ?"
            
            params = (id_empleado,)
            
            cursor = con.ejecuta_query(sql, params, cmt=True)
            
            # si borra algo avisa 
            if cursor.tmpcount > 0:
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
            for tmp in resultados:
                empleado_info = {
                    'id': tmp[0],
                    'nombre': tmp[1],
                    'primer_apellido': tmp[2],
                    'segundo_apellido': tmp[3] or '',
                    'telefono': tmp[4],
                    'email': tmp[5],
                    'inicio_contrato': tmp[6],
                    'salario': tmp[7],
                    'id_departamento': tmp[8],
                    'departamento': tmp[9]
                }
                empleados.append(empleado_info)
            
            return True, empleados
        
        except Exception as e:
            return False, f"Error al listar empleados por departamento: {e}"
        
        finally:
            if con:
                con.desconectar()
                print("Conexión (listar_por_depto) cerrada.")
