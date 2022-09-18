from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Tipos

from enum import Enum


class Simbolo:
    def __init__(self):
        self.valor = None
        self.id = None
        self.tipo = Tipos.NULL
        self.simbolo = None
        self.mut = None
        self.linea = 0
        self.columna = 0
        self.direccionRelativa = 0
        
        #----------------------FUNCION
        self.parametros = []
        self.instrucciones = []
        
        #----------------------STRUCT
        self.id_instancia = ""
        self.entornoInstancia = None
        
        #----------------------ARREGLO
        self.valores = []
        self.dimensiones = []
        
        #----------------------REFERENCIA
        self.entornoReferencia = None
        self.valorReferencia = None
        
        
        
    
    def iniciarPrimitivo(self, id: str, tipo: Tipos, valor:Expresion, direccionRelativa,  mut = False):
        self.valor = valor
        self.id = id
        self.tipo = tipo
        self.mut = mut
        self.direccionRelativa = direccionRelativa
    
    def iniciarFuncion(self, identificador,listaParametros,listaInstrucciones, tipo, ):
        self.identificador = identificador
        self.tipo = tipo
        self.parametros = listaParametros
        self.instrucciones = listaInstrucciones