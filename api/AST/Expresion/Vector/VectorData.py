from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_
from Entorno.Tipos import Tipo, Tipos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno



class VectorData(Expresion):

    def __init__(self, listaExpresiones, linea:int, columna: int):
        self.listaExpresiones = listaExpresiones
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
        
    def obtener3D(self, ts) -> Retorno:
        pass
        
        