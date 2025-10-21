import mariadb
from os import getenv
from dotenv import load_dotenv, find_dotenv
from .model import base, base_chx
load_dotenv(find_dotenv())

class rdbms:
    def __init__(self, _host:str, _user:str, _passwd: str, _database:str ,_port:int):
        self._host = _host
        self._user = _user
        self._passwd = _passwd
        self._database = _database
        self._port = _port
        
        _conf:dict = {
            'host': _host,
            'user': _user,
            'password': _passwd,
            'database': _database,
            'port': _port
        }
        
        self._cnx = mariadb.connect(**_conf)
        self._cur = self._cnx.cursor()
        
    def query(self, sql:str, data:tuple = () , row = None, cmt:bool = False):
        if cmt == False and row != None and row == int:
            self._cur.execute(sql,data)
            return self._cur.fetchall()
        elif cmt == False and row == None:
            self._cur.execute(sql,data)
            return self._cur.fetchmany(row or int())
        elif cmt == True and row == None:
            self._cur.execute(sql, data)
            self._cnx.commit()
            
    def rollback(self):
        self._cnx.rollback()
        
    def close(self):
        self._cur.close()
            
    def model_chx(self):
        try:
            self._cur.execute(base_chx, ('empleados', 'registros', 'proyectos', 'departamentos', 'roles')) # comprueba si existen las tablas de "modelo.erd"
            tmp = self._cur.fetchall()[0][0] # de una tupla con listas, se asigna el dato de la lista a la variable con doble indice -> ([0,]) -> [0,] -> 0
            if tmp != 4:
                for i in base:
                    self._cur.execute(i)
                self._cnx.commit()
                return False
            elif tmp == 4:
                print(f'Tablas encontradas: {tmp}')
                return True
        except (mariadb.ProgrammingError, mariadb.OperationalError) as e:
            return e
    
db = rdbms(
    _host= getenv('HOST') or 'localhost',
    _user= getenv('NAME') or 'root',
    _passwd= getenv('PASSWD') or '',
    _database= getenv('DATABASE') or '',
    _port= int(getenv('PORT') or '3306')
)

if __name__ == '__main__':
    db.model_chx()
