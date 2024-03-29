from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Tipos
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Generador import Generador

import copy

class CrearArreglo(Instruccion):
    def __init__(self, id_instancia:str, dimensiones, tipo, expresion, mut, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.mut = mut
        
        self.enFuncion = False
        self.puntero_nuevo = ""
        self.valorCompilado = None
        self.esReferencia = False
        
        self.declarar_en_instancia = False
         
        
    def ejecutar3D(self, ts: TablaSimbolos):
        
        # valor = self.expresion.obtener3D(ts)
        
        valor = None
        if self.expresion is not None:
            valor = self.expresion.obtener3D(ts)
        elif self.valorCompilado is not None:
            valor = self.valorCompilado
            
        PUNTERO = "SP"
        SEGMENTO = "Stack"
        
        if self.enFuncion:
            PUNTERO = self.puntero_nuevo
        
        if (valor.tipo != Tipos.ARRAY_DATA):
            
            Error_('Semantico', f'Tipo incorrecto en definicion de arreglo', ts.env, self.linea, self.columna)   
            return ""
        
        
        # if self.tipo is not None:
            
        #     print(self.tipo, " - ", valor.valor.tipo)
                
        #     if self.tipo != valor.valor.tipo:
        #         Error_('Semantico', f'Tipo incorrecto en definicion de arreglo', ts.env, self.linea, self.columna)   
        #         return ""
            
        # if self.esReferencia:
        #     temp1 = Generador.obtenerTemporal()
        # else:
        #     temp1 = Generador.obtenerTemporal()
        
        temp1 = Generador.obtenerTemporal()
        
        SALIDA = f"/* Declaracion Arreglo {self.id_instancia}*/ \n"
        SALIDA += valor.codigo
        SALIDA += f'{temp1} = {PUNTERO} + {ts.tamanio}; \n'
        SALIDA += f'{SEGMENTO}[(int){temp1}] = {valor.temporal}; \n'
        
        
        instancia = ts.buscar(self.id_instancia)
        if instancia is not None:
            Error_("Semantico", f'Ya se ha declarado el simbolo \'{self.id_instancia}\'', ts.env, self.linea, self.columna)
            return ""
        
        # print(valor.valor)
        
        nueva_instancia: InstanciaArreglo = copy.deepcopy(valor.valor) 
        nueva_instancia.identificador = self.id_instancia
        nueva_instancia.direccionRelativa = ts.tamanio
        
        ts.tamanio += 1
           
        ts.add(self.id_instancia, nueva_instancia, self.linea, self.columna)
      
        return SALIDA

       
        
        
    
            

