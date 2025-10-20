import mariadb
from os import getenv
from dotenv import load_dotenv, find_dotenv
from model import base_chx
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
        self.query(base_chx, ('empleado', 'telefono'), row= 1)
    
db = rdbms(                 # why still have ts warnings ? idk
    host= getenv('HOST'),  # type: ignore
    user= getenv('NAME'), # type: ignore
    passwd= getenv('PASSWD'), # type: ignore
    database= getenv('DATABASE'), # type: ignore
    port= int(getenv('PORT')) # type: ignore
)

if __name__ == '__main__':
    db.model_chx()