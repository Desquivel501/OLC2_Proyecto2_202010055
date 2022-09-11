from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Tipos import Tipo, Tipos
from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion


class CrearVector(Instruccion):
    def __init__(self, id_instancia:str, capacidad, tipo, expresion, mut, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.capacidad = capacidad
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.mut = mut
    
    
    def ejecutar3D(self, ts: TablaSimbolos):
        pass

    
