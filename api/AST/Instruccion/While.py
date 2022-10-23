from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from AST.misc.Display_obj import Display_obj
from Entorno.Retorno import Retorno
from Generador import Generador

class While(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts: TablaSimbolos):
        
        ts_local = TablaSimbolos(ts, "WHILE")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        SALIDA = ""
        
        ETQ_INICIO = Generador.obtenerEtiqueta()
        ETQ_SALIDA = Generador.obtenerEtiqueta()
        
        self.condicion.etiquetaVerdadera = Generador.obtenerEtiqueta();
        self.condicion.etiquetaFalsa = ETQ_SALIDA
        
        condicion = self.condicion.obtener3D(ts)
        
        if condicion.tipo != Tipos.BOOLEAN:
            Error_("Semantico", "La condicion en un while debe ser de tipo BOOLEAN", ts.env, self.linea, self.columna)
            return SALIDA
        
        
        DISPLAY = Display_obj()
        DISPLAY.inicio = ETQ_INICIO
        DISPLAY.salida = ETQ_SALIDA
        ts_local.ptr += 1
        ts_local.Display[ts_local.ptr] = DISPLAY
        
        
        SALIDA += "/* INSTRUCCION WHILE */\n"
        SALIDA += f'{ETQ_INICIO}:\n'
        SALIDA += condicion.codigo
        SALIDA += f'{self.condicion.etiquetaVerdadera}:\n'
        SALIDA += self.cuerpo.ejecutar3D(ts_local)
        SALIDA += f'goto {ETQ_INICIO};\n'
        SALIDA += f'{ETQ_SALIDA}:\n'
        
        ts_local.ptr -= 1
        
        return SALIDA
