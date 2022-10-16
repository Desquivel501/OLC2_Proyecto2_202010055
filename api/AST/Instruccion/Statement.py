from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.Instruccion.Return import Return


class Statement(Instruccion):

    def __init__(self, codigo, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna
        
        self.tipo = Tipos.VOID


    def ejecutar3D(self, ts):
        SALIDA = ""
        for ins in self.codigo :
            SALIDA += ins.ejecutar3D(ts)
            
            if isinstance(ins, Return):
                if self.tipo == Tipos.VOID:                    
                    self.tipo = ins.tipo
        
        return SALIDA

    