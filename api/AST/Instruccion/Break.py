from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.error import Error_

class Break(Instruccion):

    def __init__(self, expresion: Expresion, linea, columna):
        self.linea = linea
        self.columna = columna
        self.expresion = expresion


    def ejecutar3D(self, ts: TablaSimbolos) -> Retorno:
        SALIDA = ""
        
        if ts.ptr == 0:
            Error_("Semantico", "Break fuera de ciclo", ts.env, self.linea, self.columna)
        
        else:
            etiqueta = ts.Display[ts.ptr].salida
            SALIDA += f'/* -- BREAK -- */\n'
            SALIDA += f'goto {etiqueta};\n'
        
        return SALIDA
    
    