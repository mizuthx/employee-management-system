class ProyectoDTO:
    def __init__(self, nombre:str, descripcion:str, fecha_inicio:str,):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        
    def __str__(self) -> str:
        return f"{self.nombre}"