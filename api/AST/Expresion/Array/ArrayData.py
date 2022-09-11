from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Tipos import Tipo, Tipos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno



class ArrayData(Expresion):

    def __init__(self, listaExpresiones, linea:int, columna: int):
        self.listaExpresiones = listaExpresiones
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
    
    def obtener3D(self, ts) -> Retorno:
        pass