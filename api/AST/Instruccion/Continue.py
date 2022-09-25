from Entorno.Retorno import Retorno, Tipos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from AST.misc.error import Error_

class Continue(Instruccion):

    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts):
        SALIDA = ""
        
        if ts.ptr == 0:
            Error_("Semantico", "Break fuera de ciclo", ts.env, self.linea, self.columna)
        
        else:
            etiqueta = ts.Display[ts.ptr].inicio
            SALIDA += f'/* -- CONTINUE -- */\n'
            SALIDA += f'goto {etiqueta};\n'
        
        return SALIDA
    