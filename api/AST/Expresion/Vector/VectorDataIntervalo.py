
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_
from Entorno.Tipos import Tipo, Tipos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno



class VectorDataIntervalo(Expresion):

    def __init__(self, expresion, cantidad, linea:int, columna: int):
        self.cantidad = cantidad
        self.expresion = expresion
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
    
    def obtener3D(self, ts):
        pass
        