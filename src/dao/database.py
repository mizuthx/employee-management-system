import mariadb
from os import getenv
from dotenv import load_dotenv, find_dotenv
from model import base, base_chx, base_insert, base_views
load_dotenv(find_dotenv())

class rdbms:
    _status:bool = False
    def __init__(self, _host:str, _user:str, _passwd: str, _database:str ,_port:int):
        self._host = _host
        self._user = _user
        self._passwd = _passwd
        self._database = _database
        self._port = _port
        
        # Diccionario para las credenciales de la base de datos
        _conf:dict = {
            'host': _host,
            'user': _user,
            'password': _passwd,
            'database': _database,
            'port': _port
        }
        
        # Definiendo conexion al conector con el diccionario asignadolo
        # a _cnx, asi para poder usar '_cnx.close() _cnx.commit()' entre otros.
        try:
            self._cnx = mariadb.connect(**_conf)
            # Definidiendo el cursor para las querys utilizando la anterior definida
            # variable _cnx, queda tal que asi self._cur.*
            self._cur = self._cnx.cursor()
        except mariadb.OperationalError as e:
            print('Se produjo un error al conectar la base de datos')
            input('Presione ENTER para continuar...')

    # Metodo pensado para hacer consultas desde una linea asi haciendo mas legible el CRUD,
    # este teniendo varias intrucciones dependiendo las nececidades del proyecto,
    # por ahora execute(), fetch*(), commit(), close().
    def query(self, sql:str, data:tuple = () , row = None, cmt:bool = False):
        try:
            # Al usar query('SELECT * FROM table) retorna todas las columnas existentes
            if cmt == False and row == None:
                self._cur.execute(sql,data)
                return self._cur.fetchall()
            # Al usar query('SELECT * FROM table, row= n > 0) retorna las columnas con limites
            elif cmt == False and row != None and row == int:
                self._cur.execute(sql, data)
                return self._cur.fetchmany(row or int())
            # Al usar query('INSERT INTO table VALUES column (?, ? ,? ), (data, data, data ), cmt = True) automaticamente se genera el commit
            elif cmt == True and row == None:
                self._cur.execute(sql, data)
                self._cnx.commit()
                return self._cur.fetchall()
                
            # En caso de errores, automaticamente se cancelan las
            # transacciones pendientes
        except mariadb.Error as e:
            self._cnx.rollback()
            print(e)
    # Metodo rollback, bastante simple, quiza se propongan cambios.
    def rollback(self):
        self._cnx.rollback()
    # Metodo close, bastante simple, quiza se propongan cambios.
    def close(self):
        self._cur.close()
            
    # Creacion automatica del modelo de base de datos, por restructurar!
    def model_chx(self):
        try:
            self._cur.execute(base_chx, ('empleados', 'proyectos', 'roles', 'departamentos', 'registros'))
            tables = self._cur.fetchone()[0]
            if tables == 5:
                print('Modelo existente --> Omitiendo')
            elif tables != 5:
                for i in base:
                    self._cur.execute(i)
                self._cnx.commit()
        except (mariadb.ProgrammingError, mariadb.OperationalError) as e:
            print(e)
    def cnx_test(self):
        tmp = self._cnx.server_info
        print(tmp)

# Crea unica instancia 'db' para el uso de CRUD este mantiene
# privado las credenciales de la base de datos con dotenv, asi 
# tambien manteniendo los atributos ocultos en la clase, like
#>>> print(db._password) ---> ERROR*
db = rdbms(
    _host= getenv('HOST') or 'localhost',
    _user= getenv('NAME') or 'root',
    _passwd= getenv('PASSWD') or '',
    _database= getenv('DATABASE') or '',
    _port= int(getenv('PORT') or '3306')
)

# intruccion solo para debug, ignorar.
if __name__ == '__main__':
    pass
