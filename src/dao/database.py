import mariadb
from os import getenv
from dotenv import load_dotenv, find_dotenv
from .model import base, base_chx, base_insert, base_views
load_dotenv(find_dotenv())

class rdbms:
    _status:bool = False
    def __init__(self, host:str, user:str, passwd: str, database:str ,port:int):
        # Definiendo conexion del conector mariadb a __cnx, asi para poder usar 
        # '__cnx.close() __cnx.commit()' entre otros.
        try:
            self.__cnx = mariadb.connect(
                host= host,
                user= user,
                password= passwd,
                database= database,
                port= port
            )
            # Definidiendo el cursor para las querys utilizando la anterior definida
            # variable __cnx, queda tal que asi self.__cur.*
            self.__cur = self.__cnx.cursor()
        except mariadb.Error as e:
            print(f'Se produjo un error en la base de datos\n {e}')
            input('Presione ENTER para continuar...')
        finally:
            self.__cnx.rollback()
            self.close()

    # Metodo pensado para hacer consultas desde una linea asi haciendo mas legible el CRUD,
    # este teniendo varias intrucciones dependiendo las nececidades del proyecto,
    # por ahora execute(), fetch*(), commit(), close().
    def query(self, sql:str, data:tuple = () , row = None, cmt:bool = False):
        try:
            # Al usar query('SELECT * FROM table) retorna todas las columnas existentes
            if cmt == False and row == None:
                self.__cur.execute(sql,data)
                return self.__cur.fetchall()
            # Al usar query('SELECT * FROM table, row= n > 0) retorna las columnas con limites
            elif cmt == False and row != None and row > 0:
                self.__cur.execute(sql, data)
                return self.__cur.fetchmany(row)
            # Al usar query('INSERT INTO table VALUES column (?, ? ,? ), (data, data, data ), cmt = True) automaticamente se genera el commit
            elif cmt == True and row == None:
                self.__cur.execute(sql, data)
                self.__cnx.commit()
                return self.__cur.fetchone()
        except mariadb.Error as e:
            print(f'Se produjo un error en la base de datos\n{e}')
            input('Presione ENTER para continuar...')
        finally:
            self.__cnx.rollback()
            self.__cnx.close()
            
    # Metodo rollback, bastante simple, quiza se propongan cambios.
    def rollback(self):
        self.__cnx.rollback()
    # Metodo close, bastante simple, quiza se propongan cambios.
    def close(self):
        self.__cur.close()
            
    # Creacion automatica del modelo de base de datos, por restructurar!
    def model_chx(self):
        try:
            self.__cur.execute(base_chx, ('empleados', 'proyectos', 'roles', 'departamentos', 'registros'))
            return self.__cur.fetchone()
        except mariadb.Error as e:
            print(e)
    def cnx_test(self):
        tmp = self.__cnx.server_info
        print(tmp)

# Crea unica instancia 'db' para el uso de CRUD, este se mantiene
# en privado las credenciales de la base de datos con dotenv.
db = rdbms(
    host= getenv('HOST') or 'localhost',
    user= getenv('NAME') or 'root',
    passwd= getenv('PASSWD') or '',
    database= getenv('DATABASE') or '',
    port= int(getenv('PORT') or '3306')
)

# Solo para debug, ignorar.
if __name__ == '__main__':
    db.query('sffs')