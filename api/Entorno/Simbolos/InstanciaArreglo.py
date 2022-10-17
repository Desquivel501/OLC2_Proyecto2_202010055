
from struct import Struct
from Entorno.Simbolo import Simbolo
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Tipos

class InstanciaArreglo(Expresion, Simbolo):

    def __init__(self,tipo, dimensiones, valores):
        self.dimensiones = dimensiones
        self.valores = valores
        self.tipo = tipo
        self.identificador = None
        self.mut = False
        self.direccionRelativa = 0
        self.tipo_interno = Tipos.NULL

    def getTipo(self, ts):
        return self.tipo
    
    def getValor(self, listaDimensiones, index, valores, linea, columna):

        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            if indiceDimension > (tamanoDimension-1):
                raise Error_("Semantico", f'Índice fuera de los límites', "", linea, columna)
            else:
                subArreglo = valores[indiceDimension]
                return self.getValor(listaDimensiones, index+1, subArreglo, linea, columna)

        else:
            if indiceDimension > (tamanoDimension-1):
                raise Error_("Semantico", f'Índice fuera de los límites', "", linea, columna)
            else:
                return valores[indiceDimension]
            
        
    def modValor(self, listaDimensiones, index, valores, nuevo, linea, columna):

        if self.mut == False:
            raise Error_("Semantico", f'No se puede emodificar un arreglo constante', "", linea, columna)
        
        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            if indiceDimension > (tamanoDimension-1):
                raise Error_("Semantico", f'Índice fuera de los límites', "", linea, columna)
            else:
                subArreglo = valores[indiceDimension]
                return self.modValor(listaDimensiones, index+1, subArreglo, nuevo, linea, columna)

        else:
            if indiceDimension > (tamanoDimension-1):
               raise Error_("Semantico", f'Índice fuera de los límites', "", linea, columna)
            else:
                # if isinstance(nuevo, list):
                #     if len(valores[indiceDimension]) != len(nuevo):
                #         raise Error_("Semantico", f'Dimensiones del arreglo no coinciden', linea, columna)
                    
                valores[indiceDimension] = nuevo   