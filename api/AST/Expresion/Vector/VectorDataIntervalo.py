
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.misc.error import Error_

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador


class VectorDataIntervalo(Expresion):

    def __init__(self, expresion, cantidad, linea:int, columna: int):
        self.cantidad = cantidad
        self.expresion = expresion
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
        self.tipo = Tipos.NULL
    
    def obtener3D(self, ts) -> Retorno:
        
        SALIDA = f'/*Vector por intervalo*/\n'
        
        RETORNO = Retorno()
        
        temp1 = Generador.obtenerTemporal()
        temp2 = Generador.obtenerTemporal()
        temp3 = Generador.obtenerTemporal()
        temp4 = Generador.obtenerTemporal()
        temp5 = Generador.obtenerTemporal()
        
        etiqueta = Generador.obtenerEtiqueta()
        
        valor_exp = self.expresion.obtener3D(ts)
        valor_cant = self.cantidad.obtener3D(ts)
        
        SALIDA += valor_exp.codigo
        SALIDA += valor_cant.codigo
        
        SALIDA += f'{temp1} = HP; /*Posicion de referencia en Heap*/\n'
        
        SALIDA += f'HP = HP + 2; /* Espacio para largo y capacidad */ \n'
        SALIDA += f'HP = HP + {valor_cant.temporal}; /*Se aparta la capacidad del vector*/\n'
        
        SALIDA += f'Heap[(int){temp1}] = {valor_cant.temporal}; /*Tamaño del vector*/ \n'
        
        SALIDA += f'{temp3} = {temp1} + 1; \n'
        SALIDA += f'Heap[(int){temp3}] = {valor_cant.temporal}; /*Capacidad del vector*/ \n'
        
        
        SALIDA += f'{temp2} = 0;\n'
        SALIDA += f'{temp3} = {temp3} + 1;\n'
        
        SALIDA += f'{etiqueta}:'
        SALIDA += f'  {temp4} = {temp3} + {temp2};\n'
        SALIDA += f'  Heap[(int){temp4}] = {valor_exp.temporal};\n '
        SALIDA += f'  {temp2} = {temp2} + 1;\n'
        SALIDA += f'if({temp2} <= {valor_cant.temporal}) goto {etiqueta};\n'
        
   
        instancia = InstanciaVector(Tipos.VECTOR_DATA, [valor_cant], None)
        instancia.tipo_interno = valor_exp.tipo
        
        # print("-------------  ", instancia.tipo_interno )
        
        RETORNO.tipo_interno = valor_exp.tipo
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
    
        