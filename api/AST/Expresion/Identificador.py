
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from Entorno.Retorno import Retorno, Tipos

class Identificador(Expresion):
    
    def __init__(self, identificador: str, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        
        SALIDA = ""
        
        simbolo = ts.buscar(self.identificador)
        if simbolo is not None:
            temp1 = ts.generador.obtenerTemporal()
            temp2 = ts.generador.obtenerTemporal()
            
            SALIDA += "/* ACCESO A VARIABLE */\n"
            SALIDA += f"{temp1} = SP + {simbolo.direccionRelativa};\n"
            SALIDA += f"{temp2} = Stack[(int){temp1}];\n"
            
            retorno = Retorno()
            retorno.iniciarRetorno(SALIDA, "", temp2, simbolo.tipo)
            
            return retorno
        
        else:
            Error_("Semantico",f'No se ha encontrado la variable "{self.identificador}"',ts.env, self.linea, self.columna)
            
        
        
        