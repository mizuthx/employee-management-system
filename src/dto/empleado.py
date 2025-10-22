from datetime import date

class EmpleadoDTO:
    def __init__(self, nombre:str, primer_apellido: str, segundo_apellido:str ,numero_tel:int, direccion:str, email:str, inicio_contrato,salario:int):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.numero_tel = numero_tel
        self.direccion = direccion
        self.email = email 
        self.inicio_contrato = inicio_contrato
        self.salario = salario
    def __str__(self) -> str:
        return f"{self.nombre}"