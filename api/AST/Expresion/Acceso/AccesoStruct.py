

import copy
from  Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno

class AccesoStruct(Expresion):
    
    def __init__(self, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.linea = linea
        self.columna = columna
        
             
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        pass
        
    
    def acceso(self, listaExpresion, struct, ts) -> Retorno:
        pass
        
        
        
        
        
        