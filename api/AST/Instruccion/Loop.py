from xmlrpc.client import Boolean
from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from AST.misc.Display_obj import Display_obj


class Loop(Instruccion):

    def __init__(self, cuerpo: Statement, expresion: Boolean ,linea, columna):
        self.expresion = expresion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts):
        
        ts_local = TablaSimbolos(ts.generador, ts, "LOOP")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
                
        SALIDA = ""
        
        ETQ_INICIO = ts.generador.obtenerEtiqueta()
        ETQ_SALIDA = ts.generador.obtenerEtiqueta()
        
        DISPLAY = Display_obj()
        DISPLAY.inicio = ETQ_INICIO
        DISPLAY.salida = ETQ_SALIDA
        ts_local.ptr += 1
        ts_local.Display[ts_local.ptr] = DISPLAY
        
        
        SALIDA += "/* INSTRUCCION LOOP */\n"
        SALIDA += f'{ETQ_INICIO}:\n'
        SALIDA += self.cuerpo.ejecutar3D(ts_local)
        SALIDA += f'goto {ETQ_INICIO};\n'
        SALIDA += f'{ETQ_SALIDA}:\n'
        
        ts_local.ptr -= 1
        
        return SALIDA
            
        