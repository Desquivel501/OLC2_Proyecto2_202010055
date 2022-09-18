from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion


class CrearArreglo(Instruccion):
    def __init__(self, id_instancia:str, dimensiones, tipo, expresion, mut, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.mut = mut
         
        
    def ejecutar3D(self, ts: TablaSimbolos):
        pass
       
        
        
    
            

