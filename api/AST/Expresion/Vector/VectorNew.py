
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador

class VectorNew(Expresion):
    
    def __init__(self):
        self.tipo = None
        
    def obtener3D(self, ts):
        
        # print("here------------------------------------")
        
        SALIDA = ""
        
        RETORNO = Retorno()
        
        temp1 = Generador.obtenerTemporal()
        temp3 = Generador.obtenerTemporal()
        
        
        SALIDA += f'/*Vector por capacidad*/\n'
        
        SALIDA += f'{temp1} = HP; /*Posicion de referencia en Heap*/\n'
        

        
        SALIDA += f'HP = HP + 2; /* Espacio para largo y capacidad */ \n'
        
        SALIDA += f'Heap[(int){temp1}] = 0; /*Tamaño del vector*/ \n'
        
        SALIDA += f'{temp3} = {temp1} + 1; \n'
        SALIDA += f'Heap[(int){temp3}] = 0; /*Capacidad del vector*/ \n'
    
        instancia = InstanciaVector(Tipos.VECTOR_DATA, [], None)
        instancia.tipo_interno = Tipos.NULL
        instancia.isNew = True
        
        RETORNO.tipo_interno = Tipos.NULL
        RETORNO.iniciarRetornoArreglo(SALIDA, temp1, Tipos.VECTOR_DATA, instancia)
        
        return RETORNO 
        
    

    
