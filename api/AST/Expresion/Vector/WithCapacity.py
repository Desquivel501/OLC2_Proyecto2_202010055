
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador

class Capacidad(Expresion):
    
    def __init__(self, expresion):
        self.expresion = expresion
        
    def obtener3D(self, ts):
        
        print("here------------------------------------")
        
        SALIDA = ""
        
        RETORNO = Retorno()
        
        temp1 = Generador.obtenerTemporal()
        # temp2 = Generador.obtenerTemporal()
        temp3 = Generador.obtenerTemporal()
        
        valor_capacidad = self.expresion.obtener3D(ts)
        
        SALIDA += f'/*Vector por capacidad*/\n'
        
        SALIDA += f'{temp1} = HP; /*Posicion de referencia en Heap*/\n'
        
        SALIDA += valor_capacidad.codigo
        # SALIDA += f'{temp2} = {}'
        
        SALIDA += f'HP = HP + 2; /* Espacio para largo y capacidad */ \n'
        SALIDA += f'HP = HP + {valor_capacidad.temporal}; /*Se aparta la capacidad del vector*/\n'
        
        SALIDA += f'Heap[(int){temp1}] = 0; /*Tamaño del vector*/ \n'
        
        SALIDA += f'{temp3} = {temp1} + 1; \n'
        SALIDA += f'Heap[(int){temp3}] = {valor_capacidad.temporal}; /*Capacidad del vector*/ \n'
    
    
        instancia = InstanciaVector(Tipos.VECTOR_DATA, [valor_capacidad], None)
        instancia.tipo_interno = Tipos.NULL
        
        RETORNO.tipo_interno = Tipos.NULL
        RETORNO.iniciarRetornoArreglo(SALIDA, temp1, Tipos.VECTOR_DATA, instancia)
        
        return RETORNO 
        
    

    
