from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from Generador import Generador
from Entorno.Retorno import Tipos

class Return(Instruccion):

    def __init__(self, expresion: Expresion, linea, columna):
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.tipo = Tipos.VOID


    def ejecutar3D(self, ts):
        
        SALIDA = ""
    
        
        if self.expresion is None:
            return "goto RETORNO; \n"
        
        valor = self.expresion.obtener3D(ts)
        
        SALIDA += valor.codigo
        self.tipo = valor.tipo
        temp = Generador.obtenerTemporal()
        SALIDA += f'{temp} = SP + 0;\n'
        SALIDA += f'Stack[(int){temp}] = {valor.temporal}; \n'
        SALIDA += "goto RETORNO; \n"
        return SALIDA
    
    