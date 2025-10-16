from gestor_empleados.src.DAO.database import db




if __name__ == "__main__":
    if db.check_cnx() == True:
        print("OK")