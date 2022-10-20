

from AST.Expresion.Else import Else
from Entorno.Simbolo import Simbolo

from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador
from AST.misc.Display_obj import Display_obj


class ExpMatch(Expresion):
    def __init__(self, condicion: Expresion, case_list, default, linea, columna):
        self.condicion = condicion
        self.case_list = case_list
        self.default = default
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
        
        ts_local = TablaSimbolos(ts, "MATCH")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        RETORNO = Retorno()
        
        ETQ_SALIDA = Generador.obtenerEtiqueta()
        TEMP = Generador.obtenerTemporal()
        
        DISPLAY = Display_obj()
        DISPLAY.salida = ETQ_SALIDA
        ts.ptr += 1
        ts.Display[ts.ptr] = DISPLAY
        
        condicion = self.condicion.obtener3D(ts)
        # cond_temp = Generador.obtenerTemporal()
        
        SALIDA = "/* MATCH COMO EXPRESION */\n"
        SALIDA += condicion.codigo
        

        for case in self.case_list:
            found_etq = Generador.obtenerEtiqueta()
            next_etq = Generador.obtenerEtiqueta()
            
            SALIDA += "/* CASE EXPRESION */\n"
            
            for exp in case.lista_exp:
                valor = exp.obtener3D(ts_local)
                SALIDA += valor.codigo
                SALIDA += f'if ( {condicion.temporal} == {valor.temporal}) goto {found_etq}; \n'
            
            SALIDA += f'goto {next_etq};\n'

            SALIDA += f'{found_etq}:\n'
            # SALIDA += case.codigo.ejecutar3D(ts_local)
            valor = case.obtener3D(ts_local)
            SALIDA += valor.codigo
            SALIDA += f'{TEMP} = {valor.temporal};\n'
            
            SALIDA += f'goto {ETQ_SALIDA};\n'
            
            SALIDA += f'{next_etq}:\n'

        if self.default is not None:
            SALIDA += "/* DEFAULT */\n"
            valor_def = self.default.obtener3D(ts_local)
            SALIDA += valor_def.codigo
            SALIDA += f'{TEMP} = {valor_def.temporal};\n'
        
        SALIDA += f'{ETQ_SALIDA}:\n'
        
        
        RETORNO.iniciarRetorno(SALIDA, "", TEMP, valor.tipo)
        
        return RETORNO