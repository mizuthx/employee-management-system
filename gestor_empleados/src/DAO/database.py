import mariadb
#from model import *
from os import getenv
from dotenv import load_dotenv

load_dotenv('../../')
class rdbms:
    _status = None
    def __init__(self, host:str, user:str, passwd:str, port:int, database:str):
        self._host = host
        self._user = user
        self._passwd = passwd 
        self._port = port
        self._database = database
        
        _conf:dict = {
            'host': self._host,
            'user': self._user,
            'password': self._passwd,
            'port': self._port,
            'database': self._database
        }
        try:
            self.cnx = mariadb.connect(**_conf)
            self.cur = self.cnx.cursor()
            self._status = True
        except mariadb.Error as e:
            self._status = e
        
    def check_cnx(self):
        return self._status
    
    def query(self, sql:str, data:str = '', row= None, cmt:bool= False):
        if cmt == False and row != None:
            self.cur.execute(sql, data)
            return self.cur.fetchmany(row)
        elif cmt == True and row == None:
            self.cur.execute(sql, data)
            self.cnx.commit()

db = rdbms(
    host= getenv('HOST'),
    user= getenv('USER'),
    passwd= getenv('PASSWD'),
    port= int(getenv('PORT')),
    database= getenv('DATABASE')
)

if __name__ == '__main__':
    db.check_cnx()
    print(db.query('SELECT * FROM test'))
