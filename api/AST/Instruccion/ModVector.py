from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno, Tipos
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Generador import Generador
from Entorno.Simbolos.InstanciaVector import InstanciaVector

class ModVector(Expresion):
    
    def __init__(self, instancia, listaExpresiones, expresion, linea, columna):
        self.listaExpresiones = listaExpresiones
        # self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.instancia = instancia

             
    def ejecutar3D(self, ts):
        pass