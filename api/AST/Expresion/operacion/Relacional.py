from cmath import sqrt
from Entorno.Retorno import Retorno, Tipos
from AST.Expresion.Expresion import Expresion
from AST.misc.error import Error_

from AST.Expresion.operacion.Operacion import Operador, Operacion
from Entorno.TablaSimbolos import TablaSimbolos

class Relacional(Operacion):
    
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__(left, operador, right, linea, columna, unaria)
    
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        
        SALIDA = ""
        
        valor_left = self.left.obtener3D(ts)
        valor_right = self.right.obtener3D(ts)
        
        SALIDA += valor_left.codigo
        SALIDA += valor_right.codigo
        RETORNO = Retorno()
        
        
        if valor_left.tipo in [Tipos.INT, Tipos.FLOAT] and valor_right.tipo in [Tipos.INT, Tipos.FLOAT]:
            
            if valor_left.tipo != valor_right.tipo:
                Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
                return RETORNO
            
            SALIDA += f' if ( {valor_left.temporal} {self.op_cad} {valor_right.temporal}) goto {self.etiquetaVerdadera}; \n'
            SALIDA += f' goto {self.etiquetaFalsa}; \n'
            
        
            RETORNO.iniciarRetorno(SALIDA,"","",Tipos.BOOLEAN)
            RETORNO.etiquetaV = self.etiquetaVerdadera
            RETORNO.etiquetaF = self.etiquetaFalsa
            return RETORNO
    
    
        Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
        return RETORNO
        
                
    def getOperacion(self, op:Operador):
        if op == Operador.IGUAL:
            return "Igualacion"
        if op == Operador.NO_IGUAL:
            return "Distinto"
        if op == Operador.MAYOR:
            return "Mayor que"
        if op == Operador.MAYOR_I:
            return "Mayor o igual que"
        if op == Operador.MENOR:
            return "Menor que"
        if op == Operador.MENOR_I:
            return "Menor o igual que"
    