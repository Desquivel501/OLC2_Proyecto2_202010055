from Entorno.Simbolos.Modulo import Modulo
from AST.Expresion.Llamada import Llamada
from Entorno.TablaSimbolos import TablaSimbolos
from AST.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from AST.misc.error import Error_
from Entorno.Simbolos.Struct import Struct


class Ast:

    def __init__(self, instrucciones=None):
        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones
        self.ts = None
