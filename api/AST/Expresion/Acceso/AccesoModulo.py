
import copy
from Entorno.Simbolos.Modulo import Modulo
from  Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno

class AccesoModulo(Expresion, Instruccion):
    
    def __init__(self, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.tipo = None
        self.linea = linea
        self.columna = columna
        
    def ejecutar3D(self, ts):
       pass
        
             
    def obtener3d(self, ts: TablaSimbolos) -> Retorno:
        pass
        

    
    def acceso(self, listaExpresion, instancia, ts)  -> Retorno:
        pass
            
        
            
        
        
        
        
        
        