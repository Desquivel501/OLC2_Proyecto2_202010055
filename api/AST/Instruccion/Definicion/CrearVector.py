from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador
import copy

class CrearVector(Instruccion):
    def __init__(self, id_instancia:str, capacidad, tipo, expresion, mut, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.capacidad = capacidad
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
        
        valor = None
        if self.expresion is not None:
            valor = self.expresion.obtener3D(ts)
        elif self.valorCompilado is not None:
            valor = self.valorCompilado
            
        PUNTERO = "SP"
        SEGMENTO = "Stack"
        
        if self.enFuncion:
            PUNTERO = self.puntero_nuevo
        
        if (valor.tipo != Tipos.VECTOR_DATA):
            
            Error_('Semantico', f'Tipo incorrecto en definicion de vector', ts.env, self.linea, self.columna)   
            return ""

        
        temp1 = Generador.obtenerTemporal()
        
        SALIDA = f"/* Declaracion Vector {self.id_instancia}*/ \n"
        SALIDA += valor.codigo
        SALIDA += f'{temp1} = {PUNTERO} + {ts.tamanio}; \n'
        SALIDA += f'{SEGMENTO}[(int){temp1}] = {valor.temporal}; \n'
        
        
        instancia = ts.buscar(self.id_instancia)
        if instancia is not None:
            Error_("Semantico", f'Ya se ha declarado el simbolo \'{self.id_instancia}\'', ts.env, self.linea, self.columna)
            return ""
        
        # print(valor.valor)
        
        nueva_instancia: InstanciaVector = copy.deepcopy(valor.valor) 
        nueva_instancia.identificador = self.id_instancia
        # nueva_instancia
        nueva_instancia.direccionRelativa = ts.tamanio
        
        
        if (nueva_instancia.tipo_interno == Tipos.NULL):
            nueva_instancia.tipo_interno = self.tipo
        
        ts.tamanio += 1
           
        ts.add(self.id_instancia, nueva_instancia, self.linea, self.columna)
      
        return SALIDA

    
