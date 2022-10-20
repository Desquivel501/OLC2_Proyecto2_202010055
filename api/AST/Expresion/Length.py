
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador



class Length(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion;
        self.linea = linea
        self.columna = columna
        
        
    def obtener3D(self, ts) -> Retorno:
      
       valor = self.expresion.obtener3D(ts)
       temp = Generador.obtenerTemporal()
       
       SALIDA = "/* LENGTH */\n"
       SALIDA += valor.codigo
       SALIDA += f'{temp} = Heap[(int) {valor.temporal}];\n'
       
       RETORNO = Retorno()
       RETORNO.iniciarRetorno(SALIDA, "", temp, Tipos.INT)
       
       return RETORNO
       