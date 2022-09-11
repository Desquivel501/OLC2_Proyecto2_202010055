import copy
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Tipos import Tipo

class Asignacion(Instruccion):
    
    def __init__(self, identificador: str, valor: Expresion, tipo: Tipo, mut:bool, linea:int, columna: int , referencia = False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.mut = mut
        self.linea = linea
        self.columna = columna
        self.referencia = referencia
        self.valorCompilado = None
        
    def ejecutar3D(self, ts: TablaSimbolos):
        pass
        
        
       
        
        
    