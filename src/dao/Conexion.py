import mariadb

class Conexion:
    def __init__(self, host, user, password, port, db):
        self.db=mariadb.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            db=db)
        self.cursor=self.db.cursor()

    def ejecuta_query(self,sql, params=None, cmt=False):
        try:
            
            self.cursor.execute(sql, params)
            if cmt:
                self.commit()#hace el commit si lo pide

            return self.cursor
        
        except mariadb.Error as e:
            print(f'error de consulta: {e}')
            self.rollback()
            raise e


    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
