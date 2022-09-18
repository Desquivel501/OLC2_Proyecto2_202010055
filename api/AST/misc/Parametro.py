

from Entorno.Retorno import Tipos
class Parametro():
    
    def __init__(self, identificador: str, tipo: Tipos, referencia:bool):
        self.identificador = identificador
        self.tipo = tipo
        self.referencia = referencia
