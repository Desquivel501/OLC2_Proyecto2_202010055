
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador


class Casteo(Expresion):
    def __init__(self, nuevo_tipo: Tipos,  exp: Expresion, linea, columna):
        self.exp = exp;
        self.linea = linea
        self.columna = columna
        self.nuevo_tipo = nuevo_tipo
        
        
    def obtener3D(self, ts) -> Retorno:
        SALIDA = "/* CASTEO */\n"
        RETORNO = Retorno()
       
        valor = self.exp.obtener3D(ts)
        SALIDA += valor.codigo
       
        if valor.tipo == self.nuevo_tipo:
        #    SALIDA += f'{temp} = {valor.temporal};\n'
           RETORNO.iniciarRetorno(SALIDA, "", valor.temporal, valor.tipo)
           return RETORNO
       
        temp = Generador.obtenerTemporal()
        
        if valor.tipo == Tipos.INT and self.nuevo_tipo == Tipos.CHAR:
            SALIDA += f'{temp} = {valor.temporal};\n'
            RETORNO.iniciarRetorno(SALIDA, "", temp, Tipos.CHAR)
            return RETORNO
        
        elif valor.tipo  == Tipos.INT and self.nuevo_tipo == Tipos.FLOAT:
            SALIDA += f'{temp} = {valor.temporal};\n'
            RETORNO.iniciarRetorno(SALIDA, "", valor.temporal, Tipos.FLOAT)
            return RETORNO
        
        elif valor.tipo  == Tipos.FLOAT and self.nuevo_tipo == Tipos.INT:
            SALIDA += f'{temp} = (int){valor.temporal};\n'
            RETORNO.iniciarRetorno(SALIDA, "", valor.temporal, Tipos.INT)
            return RETORNO
        
        else:
            Error_("Semantico", f'No se puede castear de {valor.tipo} a {self.nuevo_tipo}',  ts.env, self.linea, self.columna)
       
        return Retorno()