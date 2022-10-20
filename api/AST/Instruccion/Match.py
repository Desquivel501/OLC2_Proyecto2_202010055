
from operator import truediv
from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from AST.Instruccion.Case import Case
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Generador import Generador
from AST.misc.Display_obj import Display_obj

class Match(Instruccion):

    def __init__(self, condicion: Expresion, case_list, default, linea, columna):
        self.condicion = condicion
        self.case_list = case_list
        self.default = default
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts) -> Retorno:
        
        ts_local = TablaSimbolos(ts, "MATCH")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        ETQ_SALIDA = Generador.obtenerEtiqueta()
        
        DISPLAY = Display_obj()
        DISPLAY.salida = ETQ_SALIDA
        ts.ptr += 1
        ts.Display[ts.ptr] = DISPLAY
        
        condicion = self.condicion.obtener3D(ts)
        # cond_temp = Generador.obtenerTemporal()
        
        SALIDA = "/* INSTRUCCION MATCH */\n"
        SALIDA += condicion.codigo
        
        
        for case in self.case_list:
            found_etq = Generador.obtenerEtiqueta()
            next_etq = Generador.obtenerEtiqueta()
            
            SALIDA += "/* CASE */\n"
            
            for exp in case.lista_exp:
                valor = exp.obtener3D(ts_local)
                SALIDA += valor.codigo
                SALIDA += f'if ( {condicion.temporal} == {valor.temporal}) goto {found_etq}; \n'
            
            SALIDA += f'goto {next_etq};\n'

            SALIDA += f'{found_etq}:\n'
            SALIDA += case.codigo.ejecutar3D(ts_local)
            SALIDA += f'goto {ETQ_SALIDA};\n'
            
            SALIDA += f'{next_etq}:\n'

        if self.default is not None:
            SALIDA += "/* DEFAULT */\n"
            SALIDA += self.default.ejecutar3D(ts_local)
        
        
        SALIDA += f'{ETQ_SALIDA}:\n'
        
        return SALIDA
            
            
                
                
                
        