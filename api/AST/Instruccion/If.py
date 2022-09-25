
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
        print("IF---------------------------------------------------------")
        SALIDA = ""
        
        ETQ_SALIDA = ts.generador.obtenerEtiqueta();
        
        self.condicion.etiquetaVerdadera = ts.generador.obtenerEtiqueta();
        self.condicion.etiquetaFalsa = ts.generador.obtenerEtiqueta();
        
        condicion = self.condicion.obtener3D(ts)
      
        SALIDA += "/* INSTRUCCION IF */\n"
        SALIDA += condicion.codigo
        SALIDA += f'{self.condicion.etiquetaVerdadera}:\n'
        SALIDA += self.cuerpo.ejecutar3D(ts)
        SALIDA += f'goto {ETQ_SALIDA};\n'
        SALIDA += f'{self.condicion.etiquetaFalsa}:\n'
        
        if self.else_ is not None:
            SALIDA += self.else_.ejecutar3D(ts)
        
        SALIDA += f'{ETQ_SALIDA}:\n'
        
        return SALIDA