
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Tipos import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno

class AccesoArreglo(Expresion):
    
    def __init__(self, id_instancia, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna

             
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        pass
    
    def acceso(self, ts, listaExpresiones, inctancia) -> Retorno:
        pass
            
        
        
        
        