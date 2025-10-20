import mariadb
from os import getenv
from dotenv import load_dotenv, find_dotenv
from model import base_chx, base
load_dotenv(find_dotenv())

class rdbms:
    def __init__(self, host:str, user:str, passwd: str, database:str ,port:int):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.port = port
        
        conf:dict = {
            'host': host,
            'user': user,
            'password': passwd,
            'database': database,
            'port': port
        }
        
        self.cnx = mariadb.connect(**conf)
        self.cur = self.cnx.cursor()
        
    def query(self, sql:str, data:tuple , row = None, cmt:bool = False):
        if cmt == False and row != None and row == int:
            self.cur.execute(sql,data)
            return self.cur.fetchmany(row)
        elif cmt == True and row == None:
            self.cur.execute(sql, data)
            self.cnx.commit()
            
    def model_chx(self):
        self.cur.execute(base_chx, ('empleados', 'registros', 'proyectos', 'departamentos')) # comprueba si existen las tablas de "modelo.erd"
        tmp = self.cur.fetchall()[0][0] # de una tupla con listas, se asigna el dato de la lista a la variable con doble indice -> ([0,]) -> [0,] -> 0
        if tmp != 4: 
            for i in base:
                self.cur.execute(i)
            self.cnx.commit()
        elif tmp == 4:
            print(f'Tablas encontradas: {tmp}')
        
        
        
        
    
db = rdbms(                 # why still have ts warnings ? idk
    host= getenv('HOST'),  # type: ignore
    user= getenv('USER'), # type: ignore
    passwd= getenv('PASSWD'), # type: ignore
    database= getenv('DATABASE'), # type: ignore
    port= int(getenv('PORT')) # type: ignore
)

if __name__ == '__main__':
    db.model_chx()