

from AST.Expresion.Else import Else
from Entorno.Simbolo import Simbolo

from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos

from AST.misc.error import Error_
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador

class ExpIf(Expresion):
    def __init__(self, condicion: Expresion, instrucciones , cuerpo: Expresion, else_ : Expresion, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
        self.tipo = None
        self.salida = ""
        
        
    def obtener3D(self, ts) -> Retorno:
        ts_local = TablaSimbolos(ts, "IF")
        ts_local.Display = ts.Display
        ts_local.ptr = ts.ptr
        ts_local.tamanio = ts.tamanio
        
        SALIDA = ""
        RETORNO = Retorno()
        
        ETQ_SALIDA = self.salida
        if self.salida == "":
            ETQ_SALIDA = Generador.obtenerEtiqueta();
        
        self.condicion.etiquetaVerdadera = Generador.obtenerEtiqueta();
        self.condicion.etiquetaFalsa = Generador.obtenerEtiqueta();
        
        condicion = self.condicion.obtener3D(ts)
        
        if condicion.tipo != Tipos.BOOLEAN:
            Error_("Semantico", "La condicion en un If debe ser de tipo BOOLEAN", ts.env, self.linea, self.columna)
            return RETORNO

        temp = Generador.obtenerTemporal()
        
        SALIDA += "/* IF COMO EXPRESION */\n"
        SALIDA += condicion.codigo
        SALIDA += f'{self.condicion.etiquetaVerdadera}:\n'
        
        for inst in self.instrucciones:
            SALIDA += inst.ejecutar3D(ts)
  
        valor = self.cuerpo.obtener3D(ts_local)
        SALIDA += valor.codigo
        SALIDA += f'{temp} = {valor.temporal};\n'
        
        if self.else_ is not None:
            
            SALIDA += f'goto {ETQ_SALIDA};\n'
            SALIDA += f'{self.condicion.etiquetaFalsa}:\n'    
            
            if isinstance(self.else_, ExpIf):
                self.else_.salida = ETQ_SALIDA
            
            
            if isinstance(self.else_, Else):
                
                for inst in self.else_.instruccion:
                    SALIDA += inst.ejecutar3D(ts)

            val_else = self.else_.obtener3D(ts_local)
            SALIDA += val_else.codigo
            SALIDA += f'{temp} = {val_else.temporal};\n'
            
            if self.salida == "":
                SALIDA += f'{ETQ_SALIDA}:\n'

        else:
            SALIDA += f'{self.condicion.etiquetaFalsa}:\n'
        
        RETORNO.iniciarRetorno(SALIDA, "", temp, valor.tipo)
    
        return RETORNO