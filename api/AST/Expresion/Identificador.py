
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from Entorno.Retorno import Retorno, Tipos
from Generador import Generador

class Identificador(Expresion):
    
    def __init__(self, identificador: str, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        
        self.etiquetaVerdadera = ""
        self.etiquetaFalsa = ""
        
        
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        
        SALIDA = ""
        RETORNO = Retorno()
        
        simbolo = ts.buscar(self.identificador)
        if simbolo is not None:
            temp1 = Generador.obtenerTemporal()
            temp2 = Generador.obtenerTemporal()
            
            SALIDA += "/* ACCESO A VARIABLE */\n"
            SALIDA += f"{temp1} = SP + {simbolo.direccionRelativa};\n"
            SALIDA += f"{temp2} = Stack[(int){temp1}];\n"
            
            
            if simbolo.tipo == Tipos.BOOLEAN and self.etiquetaVerdadera != "":
                SALIDA += f'if({temp2} == 1) goto {self.etiquetaVerdadera};\n'
                SALIDA += f'goto {self.etiquetaFalsa};\n '
                RETORNO.etiquetaV = self.etiquetaVerdadera
                RETORNO.etiquetaF = self.etiquetaFalsa
            
            if isinstance(simbolo, InstanciaArreglo):
                RETORNO.tipo_interno = simbolo.tipo_interno
                RETORNO.valor = simbolo
            
            RETORNO.iniciarRetorno(SALIDA, "", temp2, simbolo.tipo)
            
            return RETORNO
        
        else:
            Error_("Semantico",f'No se ha encontrado la variable "{self.identificador}"',ts.env, self.linea, self.columna)
            
        
        
        