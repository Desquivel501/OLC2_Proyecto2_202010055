from cmath import sqrt
from Entorno.Retorno import Retorno, Tipos
from AST.Expresion.Expresion import Expresion
from AST.misc.error import Error_

from AST.Expresion.operacion.Operacion import Operador, Operacion

class Logica(Operacion):
    
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__(left, operador, right, linea, columna, unaria)
    
    def obtener3D(self, ts) -> Retorno:
       pass
           
        
