from api.Entorno.Retorno import Retorno
from AST.Expresion.Expresion import Expresion
from Entorno.Tipos import definirTipo

class Primitivo(Expresion):
    def __init__(self, primitivo,tipo, linea: int, columna: int):
        self.primitivo = primitivo
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        
    def obtener3D(self, ts) -> Retorno:
       pass