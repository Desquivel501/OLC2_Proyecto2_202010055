
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador
from Entorno.Simbolos.InstanciaVector import InstanciaVector



class Length(Expresion):
    def __init__(self, id_instancia, linea, columna):
        self.id_instancia = id_instancia;
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
      
        instancia = ts.buscar(self.id_instancia.identificador)
        
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
        
        SALIDA += f'{temp1} = Stack[(int) {temp0}];  /* Posicion del vector en el heap */  \n    '
        
        SALIDA += f'{temp2} = Heap[(int) {temp1}];  /* largo del vector */\n'
       
        RETORNO = Retorno()
        RETORNO.iniciarRetorno(SALIDA, "", temp2, Tipos.INT)
        
        # # print(self.id_instancia)
        
        # # valor = self.id_instancia.obtener3D(ts)
    
        # temp0 = Generador.obtenerTemporal()    
        # temp1 = Generador.obtenerTemporal()    
        # temp2 = Generador.obtenerTemporal()   
        # # if not isinstance(instancia, InstanciaVector):
        # #     Error_('Semantico', f'Simbolo "{self.id_instancia}" no es un vector', ts.env, self.linea, self.columna)  
        # #     return ""
       
       
        # SALIDA = "/* LENGTH */\n"
        # # SALIDA += f'{temp0} = SP + {instancia.direccionRelativa};\n'
        # SALIDA += valor.codigo
        # SALIDA += f'{temp1} = Stack[(int) {valor.temporal}];  /* Posicion del vector en el heap */  \n    '
        
        
        
        # SALIDA += f'{temp2} = Heap[(int) {temp1}];  /* largo del vector */\n'
        
        # SALIDA += f'printf("++++ %f\\n", {temp2});\n'
       
        # RETORNO = Retorno()
        # RETORNO.iniciarRetorno(SALIDA, "", temp2, Tipos.INT)
       
        return RETORNO
       