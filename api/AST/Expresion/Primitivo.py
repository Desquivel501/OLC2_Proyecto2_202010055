from Entorno.Retorno import Retorno, Tipos, Tipos
from AST.Expresion.Expresion import Expresion
class Primitivo(Expresion):
    def __init__(self, valor, tipo, linea: int, columna: int):
        self.valor = valor
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        
    def obtener3D(self, ts) -> Retorno:
        salida = ""
        retorno = Retorno()
        print(self.tipo)
        
        #----------------------------------------------------------------FLOAT O INT
        if self.tipo in [Tipos.INT, Tipos.FLOAT]:
           temp = ts.generador.obtenerTemporal()
           salida += f'{temp} = {self.valor}; \n'
           retorno.iniciarRetorno(salida, "", temp, self.tipo)
           
        #----------------------------------------------------------------STRING O STR
        if self.tipo in [Tipos.STRING, Tipos.STR]:
            temp = ts.generador.obtenerTemporal()
            salida += f'{temp} = HP; \n'
           
            for char in self.valor:
               valor = ord(char)
               salida += f'Heap[HP] = {valor}; \n'
               salida += f'HP = HP + 1; \n'
            
            salida += f'Heap[HP] = 0; \n'
            salida += f'HP = HP + 1; \n'
            retorno.iniciarRetorno(salida, "", temp, self.tipo)
    
        #----------------------------------------------------------------BOOLEAN
        if self.tipo == Tipos.BOOLEAN:
            temp = ts.generador.obtenerTemporal()
            if self.valor:
                salida += f'{temp} = 1; \n'
            else:
                salida += f'{temp} = 0; \n'
                
            retorno.iniciarRetorno(salida, "", temp, self.tipo)
        
        return retorno