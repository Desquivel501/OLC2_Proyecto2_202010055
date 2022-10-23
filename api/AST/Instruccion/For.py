from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo

from Entorno.Simbolo import Simbolo
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos
from AST.misc.Display_obj import Display_obj
from Generador import Generador
from AST.Expresion.Identificador import Identificador
from AST.Instruccion.Definicion.Asignacion import Asignacion

class For(Instruccion):

    def __init__(self, iterador, cuerpo: Statement, linea, columna, rango = None, lista = None):
        self.rango = rango
        self.lista = lista
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
        self.iterador = iterador


    def ejecutar3D(self, ts):
        
        ts_local = TablaSimbolos(ts, "FOR")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        ETQ_INICIO = Generador.obtenerEtiqueta()
        ETQ_SALIDA = Generador.obtenerEtiqueta()
        
        DISPLAY = Display_obj()
        DISPLAY.inicio = ETQ_INICIO
        DISPLAY.salida = ETQ_SALIDA
        ts_local.ptr += 1
        ts_local.Display[ts_local.ptr] = DISPLAY

            
        if self.rango is not None:
            
            valor_inicio = self.rango.inicio.obtener3D(ts)
            valor_fin = self.rango.fin.obtener3D(ts)
            
            
            if valor_inicio.tipo != Tipos.INT or valor_fin.tipo != Tipos.INT:
                Error_("Semantico", "Rango de For debe de ser i64", ts.env, self.linea, self.columna)
                ts_local.ptr -= 1
                return ""
            
            
            SALIDA = "/* INSTRUCCION FOR RANGO */\n"
            
            SALIDA += valor_inicio.codigo
            SALIDA += valor_fin.codigo
            
            iterador = Generador.obtenerTemporal()
            temp = Generador.obtenerTemporal()
            
            SALIDA += "/* DECLARAR ITERADOR */\n"
            SALIDA += f"{temp} = SP + {ts_local.tamanio};\n"
            SALIDA += f"Stack[(int){temp}] = {valor_inicio.temporal};\n"
                
            simbolo = Simbolo()
            simbolo.iniciarPrimitivo(self.iterador, Tipos.INT, None , ts_local.tamanio, True)  
            ts_local.add(self.iterador,simbolo,self.linea, self.columna)
            ts_local.tamanio += 1
            
            
            SALIDA += f'{ETQ_INICIO}:\n'
            SALIDA += f'{iterador} = Stack[(int){temp}];\n'
            
            SALIDA += f'if({iterador} >= {valor_fin.temporal}) goto {ETQ_SALIDA};\n'
            
            SALIDA += "\n/* CUERPO */\n"
            SALIDA += self.cuerpo.ejecutar3D(ts_local)
            SALIDA += "/* FIN CUERPO */\n"
            
            SALIDA += "\n/* AVANZAR ITERADOR */\n"
            SALIDA += f'{iterador} = Stack[(int){temp}];\n'
            SALIDA += f'{iterador} = {iterador} + 1;\n'
            SALIDA += f'Stack[(int){temp}] = {iterador};\n'
            SALIDA += f'goto {ETQ_INICIO};\n'
            SALIDA += f'{ETQ_SALIDA}:\n'
            
            ts_local.ptr -= 1
            
            return SALIDA

        
        
        