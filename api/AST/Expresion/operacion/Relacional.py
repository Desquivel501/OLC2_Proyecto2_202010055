from cmath import sqrt
from Entorno.Retorno import Retorno
from AST.Expresion.Expresion import Expresion
from AST.misc.error import Error_
from Entorno.Tipos import Tipos, definirTipo
from AST.Expresion.operacion.Operacion import Operador, Operacion

class Relacional(Operacion):
    
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__(left, operador, right, linea, columna, unaria)
    
    def obtener3D(self, ts) -> Retorno:
       pass
               
                
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
    