from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno

class GetCapacity(Expresion):
    
    def __init__(self, id_instancia,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        
    def obtener3D(self, ts) -> Retorno:
       pass
        
   