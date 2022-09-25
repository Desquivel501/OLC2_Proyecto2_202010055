from Entorno.Retorno import Retorno, Tipos, Tipos
from AST.Expresion.Expresion import Expresion
class Primitivo(Expresion):
    def __init__(self, valor, tipo, linea: int, columna: int):
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        
        self.etiquetaVerdadera = ""
        self.etiquetaFalsa = ""
        
    def obtener3D(self, ts) -> Retorno:
        SALIDA = ""
        RETORNO = Retorno()
        print(self.tipo)
        
        temp = ts.generador.obtenerTemporal()
        
        #----------------------------------------------------------------FLOAT O INT
        if self.tipo in [Tipos.INT, Tipos.FLOAT]:
           
           SALIDA += f'{temp} = {self.valor}; \n'
           RETORNO.iniciarRetorno(SALIDA, "", temp, self.tipo)
           
        #----------------------------------------------------------------STRING O STR
        if self.tipo in [Tipos.STRING, Tipos.STR]:
            SALIDA += f'{temp} = HP; \n'
           
            for char in self.valor:
               valor = ord(char)
               SALIDA += f'Heap[HP] = {valor}; \n'
               SALIDA += f'HP = HP + 1; \n'
            
            SALIDA += f'Heap[HP] = 0; \n'
            SALIDA += f'HP = HP + 1; \n'
            RETORNO.iniciarRetorno(SALIDA, "", temp, self.tipo)
    
        #----------------------------------------------------------------BOOLEAN
        if self.tipo == Tipos.BOOLEAN:
            
            if self.etiquetaVerdadera != "" and self.valor:
                SALIDA += f'goto {self.etiquetaVerdadera}; \n'
                RETORNO.etiquetaV = self.etiquetaVerdadera
                RETORNO.etiquetaV = self.etiquetaFalsa
            
            elif self.etiquetaFalsa != "" and not self.valor:
                SALIDA += f'goto {self.etiquetaFalsa}; \n'
                RETORNO.etiquetaV = self.etiquetaVerdadera
                RETORNO.etiquetaV = self.etiquetaFalsa
            
            else:
                if self.valor:
                    SALIDA += f'{temp} = 1; \n'
                else:
                    SALIDA += f'{temp} = 0; \n'
                
            RETORNO.iniciarRetorno(SALIDA, "", temp, self.tipo)
        
        return RETORNO