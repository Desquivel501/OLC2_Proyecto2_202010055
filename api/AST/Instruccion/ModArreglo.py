
from Entorno.Retorno import Retorno
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

class ModArreglo(Instruccion):
    
    def __init__(self, id_instancia, listaExpresiones, expresion ,linea, columna):
        self.listaExpresiones = listaExpresiones
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.tipo = None
        self.expresion = expresion
        
             
    def ejecutar3D(self, ts):
        pass
    
    def obtenerDimensiones(self, ts):
        pass
        