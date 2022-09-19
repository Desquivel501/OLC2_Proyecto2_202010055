
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo


class Asignacion(Instruccion):
    
    def __init__(self, identificador: str, valor: Expresion, tipo: Tipos, mut:bool, linea:int, columna: int , referencia = False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.mut = mut
        self.linea = linea
        self.columna = columna
        
        self.referencia = referencia
        self.valorCompilado = None
        
    def ejecutar3D(self, ts: TablaSimbolos):

        SALIDA = ""
        
        valor = self.valor.obtener3D(ts)
        
        
        if self.tipo is not None:
            if self.tipo != valor.tipo:
                Error_('Semantico', f'El valor de la variable no coincide con su tipo: {self.tipo} -> {valor.tipo}', ts.env, self.linea, self.columna)
                return
        else:
            self.tipo = valor.tipo
        
        
        simbolo = ts.buscar(self.identificador)
        
        if simbolo is None:
            tamanioTS = ts.tamanio
            temp = ts.generador.obtenerTemporal()
                
            SALIDA += "/* DECLARACION  VARIABLE */\n"
            SALIDA += valor.codigo
            SALIDA += f"{temp} = SP + {tamanioTS};\n"
            SALIDA += f"Stack[(int){temp}] = {valor.temporal};\n"
                
            simbolo = Simbolo()
            simbolo.iniciarPrimitivo(self.identificador, self.tipo, self.valor, tamanioTS, self.mut)  
            ts.add(self.identificador,simbolo,self.linea, self.columna)
            ts.tamanio += 1
            
            ts.generador.agregarInstruccion(SALIDA) 
            
            
        else:
            
            if  simbolo.tipo != valor.tipo:
                Error_('Semantico', f'El valor de la variable no coincide con su tipo: {simbolo.tipo} -> {valor.tipo}', ts.env, self.linea, self.columna)     
                return
            
            elif simbolo.mut is False:
                Error_("Semantico", "No se puede cambiar el valor de una constante", ts.env, self.linea, self.columna)    
                return
            
            else:
                tamanioTS = ts.tamanio
                temp = ts.generador.obtenerTemporal()
                
                SALIDA += "/* RE-DECLARACION  VARIABLE */\n"
                SALIDA += valor.codigo
                SALIDA += f"{temp} = SP + {simbolo.direccionRelativa};\n"
                SALIDA += f"Stack[(int){temp}] = {valor.temporal};\n"
                    
                simbolo = Simbolo()
                simbolo.iniciarPrimitivo(self.identificador, self.tipo, self.valor, tamanioTS, self.mut)  
                ts.add(self.identificador,simbolo,self.linea, self.columna)
                
                ts.generador.agregarInstruccion(SALIDA) 
                 
        

        
       
        
        
    