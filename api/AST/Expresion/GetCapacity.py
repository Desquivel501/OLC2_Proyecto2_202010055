from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador

class GetCapacity(Expresion):
    
    def __init__(self, id_instancia,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        
    def obtener3D(self, ts) -> Retorno:

        instancia = ts.buscar(self.id_instancia)
        
        if instancia is None:
            Error_('Semantico', f'Arreglo "{self.id_instancia}" no ha sido declarado', ts.env, self.linea, self.columna)  
            return ""
    
        temp0 = Generador.obtenerTemporal()    
        temp1 = Generador.obtenerTemporal()    
        temp2 = Generador.obtenerTemporal()   
        # if not isinstance(instancia, InstanciaVector):
        #     Error_('Semantico', f'Simbolo "{self.id_instancia}" no es un vector', ts.env, self.linea, self.columna)  
        #     return ""
       
       
        SALIDA = "/* LENGTH */\n"
        SALIDA += f'{temp0} = SP + {instancia.direccionRelativa};\n'
        
        SALIDA += f'{temp1} = Stack[(int) {temp0}];  /* Posicion del vector en el heap */  \n'
        SALIDA += f'{temp1} = {temp1} + 1;\n'
        
        SALIDA += f'{temp2} = Heap[(int) {temp1}];  /* largo del vector */\n'
       
        RETORNO = Retorno()
        RETORNO.iniciarRetorno(SALIDA, "", temp2, Tipos.INT)
       
        return RETORNO
        
   