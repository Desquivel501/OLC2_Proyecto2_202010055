from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador



class ArrayDataIntervalo(Expresion):

    def __init__(self, expresion, cantidad, linea:int, columna: int):
        self.cantidad = cantidad
        self.expresion = expresion
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna

    def obtener3D(self, ts) -> Retorno:
        SALIDA = ""
        
        RETORNO = Retorno()
        
        temp1 = Generador.obtenerTemporal()
        temp2 = Generador.obtenerTemporal()
        
        SALIDA += f'{temp1} = HP; /*Posicion de referencia en Heap*/\n'
    
        expresiones_compiladas = self.compilarExpresiones(ts)
        
        if expresiones_compiladas is None:
            return RETORNO
        
        self.listaDimensiones.append(len(expresiones_compiladas))
        
        SALIDA += f'HP = HP + {len(expresiones_compiladas) + 1};\n'
        SALIDA += f'Heap[(int){temp1}] = {len(expresiones_compiladas)}; /*Tamaño del arreglo*/ \n'
        
        i = 1
        for exp in expresiones_compiladas:
            
            if(exp.tipo == Tipos.ARRAY_DATA):
                SALIDA +=  "\n/* Referencia a un sub-arreglo*/\n"
                
                if i == 1:
                    self.listaDimensiones.extend(exp.valor.dimensiones)
            else:
                SALIDA +=  "\n/* Referencia a primitivo*/\n"
            
            SALIDA += exp.codigo
            SALIDA += f'{temp2} = {temp1} + {i}; \n'
            SALIDA += f'Heap[(int){temp2}] = {exp.temporal}; \n'
            
            i += 1
        
        instancia = InstanciaArreglo(self.tipo, self.listaDimensiones, None)
        
        RETORNO.iniciarRetornoArreglo(SALIDA, temp1, Tipos.ARRAY_DATA, instancia)
        
        return RETORNO 
            
    
    def compilarExpresiones(self, ts):
        expresiones_compiladas = []
        
        i = 0
        for exp in self.listaExpresiones:
            
            res = exp.obtener3D(ts)
            
            if i == 0:
                self.tipo = res.tipo
            else:
                if self.tipo != res.tipo:
                    Error_('Semantico', f'Tipos en arreglo no coinciden', ts.env, self.linea, self.columna)    
                    return None 
            
            expresiones_compiladas.append(res)
            i += 1
        
        return expresiones_compiladas
        
        