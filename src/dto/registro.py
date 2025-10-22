class RegistroDTO:
    def __init__(self, fecha_inicio:str, horas:int, descripcion:str, ):
        self.fecha_inicio = fecha_inicio
        self.horas = horas 
        self.descripcion = descripcion

    def __str__(self) -> str:
        return f"{self.fecha_inicio}"