
from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Statement import Statement
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from AST.misc.Program import Program
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from AST.Expresion.operacion.Relacional import Relacional
from Generador import Generador


class If(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, else_ : Instruccion, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna
        self.salida = ""


    def ejecutar3D(self, ts: TablaSimbolos):
        
        ts_local = TablaSimbolos(ts, "IF")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        SALIDA = ""
        
        ETQ_SALIDA = self.salida
        if self.salida == "":
            ETQ_SALIDA = Generador.obtenerEtiqueta();
        
        self.condicion.etiquetaVerdadera = Generador.obtenerEtiqueta();
        self.condicion.etiquetaFalsa = Generador.obtenerEtiqueta();
        
        condicion = self.condicion.obtener3D(ts)
        
        if condicion.tipo != Tipos.BOOLEAN:
            Error_("Semantico", "La condicion en un If debe ser de tipo BOOLEAN", ts.env, self.linea, self.columna)
            return SALIDA
      
        SALIDA += "/* INSTRUCCION IF */\n"
        SALIDA += condicion.codigo
        SALIDA += f'{self.condicion.etiquetaVerdadera}:\n'
        SALIDA += self.cuerpo.ejecutar3D(ts_local)
        
        if self.else_ is not None:
            
            SALIDA += f'goto {ETQ_SALIDA};\n'
            SALIDA += f'{self.condicion.etiquetaFalsa}:\n'    
            
            if isinstance(self.else_, If):
                self.else_.salida = ETQ_SALIDA
                    
            SALIDA += self.else_.ejecutar3D(ts_local)
            
            if self.salida == "":
                SALIDA += f'{ETQ_SALIDA}:\n'

        else:
            SALIDA += f'{self.condicion.etiquetaFalsa}:\n'
        
    
        return SALIDA