from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno, Tipos

class Insert(Instruccion):
    
    def __init__(self, id_instancia, expresion, indice,  linea, columna):
        self.expresion = expresion
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.indice = indice
        
             
    def ejecutar3D(self, ts):
        pass
        
        
        