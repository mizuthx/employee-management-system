# silly script, only for model_chx() of database
base_chx:str = ("""
SELECT COUNT(*) as tablas_existentes
FROM information_schema.TABLES 
WHERE TABLE_SCHEMA = DATABASE() 
AND TABLE_NAME IN (?, ?, ?, ?);
""")
    
base:list = [
    # Crear tabla departamentos
    """CREATE TABLE IF NOT EXISTS departamentos
    (
      id_departamento INT NOT NULL AUTO_INCREMENT,
      nombre VARCHAR(45) NOT NULL,
      descripcion VARCHAR(500) NULL,
      PRIMARY KEY (id_departamento)
    )""",
    
    # Constraint unique para departamentos.nombre
    """ALTER TABLE departamentos
       ADD CONSTRAINT UQ_nombre_dept UNIQUE (nombre)""",
    
    # Crear tabla empleados
    """CREATE TABLE IF NOT EXISTS empleados
    (
      id_empleado INT NOT NULL AUTO_INCREMENT,
      nombre VARCHAR(20) NOT NULL,
      primer_apellido VARCHAR(20) NOT NULL,
      segundo_apellido VARCHAR(20) NULL,
      telefono VARCHAR(11) NOT NULL,
      email VARCHAR(50) NOT NULL,
      inicio_contrato DATE NOT NULL,
      salario INT NOT NULL,
      id_departamento INT NOT NULL,
      PRIMARY KEY (id_empleado)
    )""",
    
    # Crear tabla proyectos
    """CREATE TABLE IF NOT EXISTS proyectos
    (
      id_proyecto INT NOT NULL AUTO_INCREMENT,
      id_empleado INT NOT NULL,
      nombre VARCHAR(45) NOT NULL,
      descripcion VARCHAR(500) NOT NULL,
      fecha_inicio DATE NOT NULL,
      PRIMARY KEY (id_proyecto)
    )""",
    
    # Constraint unique para proyectos.nombre
    """ALTER TABLE proyectos
       ADD CONSTRAINT UQ_nombre_proy UNIQUE (nombre)""",
    
    # Crear tabla registros
    """CREATE TABLE IF NOT EXISTS registros
    (
      id_registro INT NOT NULL AUTO_INCREMENT,
      id_empleado INT NOT NULL,
      fecha_inicio DATE NOT NULL,
      horas INT NOT NULL,
      descripcion VARCHAR(500) NOT NULL,
      PRIMARY KEY (id_registro)
    )""",
    
    # Foreign Key: empleados -> departamentos
    """ALTER TABLE empleados
       ADD CONSTRAINT FK_departamentos_TO_empleados
       FOREIGN KEY (id_departamento)
       REFERENCES departamentos (id_departamento)""",
    
    # Foreign Key: proyectos -> empleados
    """ALTER TABLE proyectos
       ADD CONSTRAINT FK_empleados_TO_proyectos
       FOREIGN KEY (id_empleado)
       REFERENCES empleados (id_empleado)""",
    
    # Foreign Key: registros -> empleados
    """ALTER TABLE registros
       ADD CONSTRAINT FK_empleados_TO_registros
       FOREIGN KEY (id_empleado)
       REFERENCES empleados (id_empleado)"""
]