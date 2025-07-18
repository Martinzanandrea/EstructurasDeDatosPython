class Temporada:
    def __init__(self,anio:int) :
        self.anio=anio
    
    def __str__(self) -> str:
        return f"ANIO: {self.anio}"
     
                    
    def __eq__(self, other) -> bool:
        if isinstance(other,Temporada):
            return (self.anio==other.anio)
    
    def __repr__(self) -> str:
       return f"ANIO: {self.anio}"
                 