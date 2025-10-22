class DepartamentoDTO:
    def __init__(self, nombre:str,descripcion:str,  ):
        self.nombre = nombre
        self.descripcion = descripcion

        def __str__(self) -> str:
            return f"{self.nombre}"