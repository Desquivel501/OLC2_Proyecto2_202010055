

from AST.misc.Program import Program
from Entorno.Simbolo import Simbolo
from AST.Instruccion.Statement import Statement
from AST.misc.error import Error_
from Entorno.Retorno import Tipos
from AST.Instruccion.Instruccion import Instruccion
from Generador import Generador

class Funcion(Simbolo, Instruccion):
    
    def __init__(self, identificador: str, lista_param, instrucciones: Statement, tipo: Tipos, linea:int, columna: int ):
        self.identificador = identificador
        self.lista_param = lista_param
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
        self.generada = False
        self.entornoFuncion = None
    
    
    def ejecutarFuncion(self, ts):            
        funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is None:
            ts.agregarFuncion(self.identificador, self)
        else:
            Error_("Semantico", f'Funcion {self.identificador} ya ha sido declarada', ts.env, self.linea, self.columna)
        

    def ejecutarParametros(self, entorno, expresiones, entorno_padre, puntero):
        
        SALIDA = ""
        
        if len(self.lista_param) != len(expresiones):
            Error_("Semantico", f'Cantidad de parametros incorrecto', "", self.linea, self.columna)
        
        i = 0
        for i in range(len(expresiones)):

            
            declaracion = self.lista_param[i]
            expresion = expresiones[i].obtener3D(entorno_padre)
            
            if declaracion.tipo != expresion.tipo:
                Error_("Semantico", f'Tipo incorrecto en parametro {self.lista_param[i].identificador}', entorno.env, self.linea, self.columna)
            
            declaracion.valorCompilado = expresion
            declaracion.puntero_nuevo = puntero
            declaracion.enFuncion = True
            SALIDA += declaracion.ejecutar3D(entorno)
        
        return SALIDA

    
    def ejecutar3D(self, ts):
        SALIDA = ""
        ETQ_RETURN = Generador.obtenerEtiqueta()
        SALIDA += f'void {self.identificador}(){{ \n'
        
        SALIDA += self.instrucciones.ejecutar3D(ts)
        
        print(self.instrucciones.tipo, " --- ", self.tipo)
        
        if self.instrucciones.tipo != self.tipo:
            Error_("Semantico", f'Tipo incorrecto en Return', ts.env, self.linea, self.columna)
            
        
        SALIDA = SALIDA.replace("RETORNO", ETQ_RETURN)
        
        SALIDA += f'{ETQ_RETURN}: \n'
        SALIDA += "return;\n"
        SALIDA += "}\n"
        return SALIDA
            
    # def ejecutarFuncion(self, ts_local):
    #     pass
        
    