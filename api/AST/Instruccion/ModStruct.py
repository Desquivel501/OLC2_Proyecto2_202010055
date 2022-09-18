


import copy
from Entorno.Retorno import Retorno, Tipos
from AST.Expresion.Identificador import Identificador
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from AST.misc.error import Error_
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

class ModStruct(Instruccion):
    
    def __init__(self, listaExpresiones, valor:Expresion, linea:int, columna:int):
        self.listaExpresiones = listaExpresiones
        self.linea = linea
        self.columna = columna
        self.valor = valor
        
     
    def ejecutar3D(self, ts):
        pass
                    
        
    
    def acceso(self, listaExpresion, struct, ts):
        pass
            
        
        
        
        
        
        