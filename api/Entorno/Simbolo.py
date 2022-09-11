from AST.Expresion.Expresion import Expresion
from Entorno.Tipos import Tipo
from enum import Enum


class Simbolo:
    def __init__(self):
        self.valor = None
        self.id = None
        self.tipo = None
        self.simbolo = None
        self.mut = None
        self.linea = 0
        self.columna = 0
        
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
        
        
        
    
    def iniciarPrimitivo(self, id: str, tipo: Tipo, valor:Expresion, mut:bool):
        self.valor = valor
        self.id = id
        self.tipo = tipo
        self.mut = mut
        