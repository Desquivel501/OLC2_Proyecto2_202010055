

from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.Struct import Struct
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion


class CrearInstanciaStruct(Instruccion):
    def __init__(self, id_instancia:str, instancia, mut:bool, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.instancia = instancia
        self.mut = mut
        self.linea = linea
        self.columna = columna
        
         
        
    def ejecutar3D(self, ts: TablaSimbolos):
        pass
