from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Retorno, Tipos
from Entorno.TablaSimbolos import TablaSimbolos
from Generador import Generador


class Case(Instruccion):

    def __init__(self, lista_exp, codigo: Instruccion, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna
        self.lista_exp = lista_exp


    def ejecutar3D(self, ts) -> Retorno:
        pass
        
        
    
    