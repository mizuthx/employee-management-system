from datetime import date

class EmpleadoDTO:
    def __init__(self, nombre:str, numero_tel:int, direccion:str, email:str, inicio_contrato,salario:int):
        self.nombre = nombre
        self.numero_tel = numero_tel
        self.direccion = direccion
        self.email = email 
        self.inicio_contrato = inicio_contrato
        self.salario = salario
    def __str__(self) -> str:
        return f"{self.nombre}"