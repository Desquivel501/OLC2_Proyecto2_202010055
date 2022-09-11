
from Entorno.Simbolos.Funcion import Funcion
from AST.Instruccion.Statement import Statement
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

class Modulo(Instruccion):
    
    def __init__(self, identificador:str, instrucciones, linea:int, columna: int ):
        self.identificador = identificador
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
        self.entorno = None
        self.publico = False
        self.esTabla = False
        
    def ejecutar(self, ts):
        
        modulo = ts.obtenerModulo(self.identificador)
        
        if modulo is not None:
            raise Error_("Semantico", f'Modulo {self.identificador} ya ha sido declarada', ts.env, self.linea, self.columna)
        
        self.entorno = ts.nuevoEntornoMod(self.identificador)
        
        for instruccion in self.instrucciones:
            
            if isinstance(instruccion, Funcion):
                if self.esTabla:
                    if instruccion.identificador == "crear_tabla":
                        instruccion.esCrearTabla = True
            
            if isinstance(instruccion, Modulo):
                if not self.esTabla:
                    instruccion.esTabla = True
            
            
            instruccion.ejecutar(self.entorno)
        
        ts.agregarModulo(self.identificador, self)
    