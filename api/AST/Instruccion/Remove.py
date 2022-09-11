from api.Entorno.Retorno import Retorno
from AST.Expresion.Identificador import Identificador
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

class Remove(Instruccion, Expresion):
    
    def __init__(self, id_instancia, indice,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.indice = indice
        
    
    def ejecutar3D(self, ts):
        pass
        
             
    def obtener3D(self, ts) -> Retorno:
       pass 
        
        
        
        