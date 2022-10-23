from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador



class VectorData(Expresion):

    def __init__(self, listaExpresiones, linea:int, columna: int):
        self.listaExpresiones = listaExpresiones
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
        self.tipo = Tipos.NULL
        self.tipo_interno = Tipos.NULL
        
        
    def obtener3D(self, ts) -> Retorno:
        SALIDA = ""
        
        RETORNO = Retorno()
        
        temp1 = Generador.obtenerTemporal()
        temp2 = Generador.obtenerTemporal()
        temp3 = Generador.obtenerTemporal()
        
        
    
        expresiones_compiladas = self.compilarExpresiones(ts)
        
        if expresiones_compiladas is None:
            return RETORNO
        
        self.listaDimensiones.append(len(expresiones_compiladas))
        
        # print("***********", self.tipo_interno)
        
        SALIDA += f'{temp1} = HP; /*Posicion de referencia en Heap*/\n'
        SALIDA += f'HP = HP + {len(expresiones_compiladas) + 2};\n'
        SALIDA += f'Heap[(int){temp1}] = {len(expresiones_compiladas)}; /*Tamaño del vector*/ \n'
        
        SALIDA += f'{temp3} = {temp1} + 1; \n'
        SALIDA += f'Heap[(int){temp3}] = {len(expresiones_compiladas)}; /*Capacidad del vector*/ \n'
        
        i = 2
        for exp in expresiones_compiladas:
            
            if(exp.tipo == Tipos.VECTOR_DATA):
                SALIDA +=  "\n/* Referencia a un sub-vector*/\n"
                
                if i == 2:
                    self.listaDimensiones.extend(exp.valor.dimensiones)
            else:
                SALIDA +=  "\n/* Referencia a primitivo*/\n"
            
            SALIDA += exp.codigo
            SALIDA += f'{temp2} = {temp1} + {i}; \n'
            SALIDA += f'Heap[(int){temp2}] = {exp.temporal}; \n'
            
            i += 1
        
        instancia = InstanciaVector(Tipos.VECTOR_DATA, self.listaDimensiones, None)
        instancia.tipo_interno = self.tipo_interno
        
        RETORNO.tipo_interno = self.tipo_interno
        RETORNO.iniciarRetornoArreglo(SALIDA, temp1, Tipos.VECTOR_DATA, instancia)
        
        
        return RETORNO 
            
    
    def compilarExpresiones(self, ts):
        expresiones_compiladas = []
        
        i = 0
        for exp in self.listaExpresiones:
            
            res = exp.obtener3D(ts)
            
            if i == 0:
                self.tipo = res.tipo
                
                if self.tipo is Tipos.VECTOR_DATA:
                    self.tipo_interno = res.tipo_interno
                else:
                    self.tipo_interno = res.tipo
                    
            else:
                if self.tipo != res.tipo:
                    Error_('Semantico', f'Tipos en arreglo no coinciden', ts.env, self.linea, self.columna)    
                    return None 
            
            expresiones_compiladas.append(res)
            i += 1
        
        return expresiones_compiladas
    
    
        
        