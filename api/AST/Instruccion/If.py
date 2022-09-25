
from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from AST.Expresion.operacion.Relacional import Relacional


class If(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, else_ : Statement, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna


    def ejecutar3D(self, ts: TablaSimbolos):
        
        ts_local = TablaSimbolos(ts.generador, ts, "IF")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        SALIDA = ""
        ETQ_SALIDA = ts.generador.obtenerEtiqueta();
        
        self.condicion.etiquetaVerdadera = ts.generador.obtenerEtiqueta();
        self.condicion.etiquetaFalsa = ts.generador.obtenerEtiqueta();
        
        condicion = self.condicion.obtener3D(ts)
        
        if condicion.tipo != Tipos.BOOLEAN:
            print(condicion.tipo)
            Error_("Semantico", "La condicion en un If debe ser de tipo BOOLEAN", ts.env, self.linea, self.columna)
            return SALIDA
      
        SALIDA += "/* INSTRUCCION IF */\n"
        SALIDA += condicion.codigo
        SALIDA += f'{self.condicion.etiquetaVerdadera}:\n'
        SALIDA += self.cuerpo.ejecutar3D(ts_local)
        
        if self.else_ is not None:
            SALIDA += f'goto {ETQ_SALIDA};\n'
            SALIDA += f'{self.condicion.etiquetaFalsa}:\n'
            SALIDA += self.else_.ejecutar3D(ts_local)
            SALIDA += f'{ETQ_SALIDA}:\n'
        
        else:
            SALIDA += f'{self.condicion.etiquetaFalsa}:\n'
        
    
        return SALIDA