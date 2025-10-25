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
        
    @staticmethod
    def listar_empleados():
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
    
    @staticmethod
    def buscar_empleado(e):
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
            """, (e.id_empleado, ), tmp= 1)
            
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

    @staticmethod
    def actualizar(e):
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
        
    @staticmethod
    def listar_por_departamento(e):
        
        resultados = db.query(
            """
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
            """,
        (e.id_departamento, ))   
        
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