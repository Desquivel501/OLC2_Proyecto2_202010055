from cmath import sqrt
from Entorno.Retorno import Retorno, Tipos
from AST.Expresion.Expresion import Expresion
from AST.misc.error import Error_

from AST.Expresion.operacion.Operacion import Operador, Operacion
from Entorno.TablaSimbolos import TablaSimbolos

class Logica(Operacion):
    
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__(left, operador, right, linea, columna, unaria)
    
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
       
        RETORNO = Retorno()
        SALIDA = ""
        

        if self.operador == Operador.NOT:
            
            self.left.etiquetaVerdadera = self.etiquetaFalsa
            self.left.etiquetaFalsa = self.etiquetaVerdadera
            
            valor_left = self.left.obtener3D(ts)
            
            RETORNO.codigo += valor_left.codigo
            RETORNO.etiquetaV = self.etiquetaVerdadera
            RETORNO.etiquetaF = self.etiquetaFalsa
            RETORNO.tipo = Tipos.BOOLEAN
            return RETORNO


        if self.operador == Operador.AND:
            
            self.left.etiquetaVerdadera = ts.generador.obtenerEtiqueta()
            self.left.etiquetaFalsa = self.etiquetaFalsa
            
            self.right.etiquetaVerdadera = self.etiquetaVerdadera
            self.right.etiquetaFalsa = self.etiquetaFalsa
            
            valor_left = self.left.obtener3D(ts)
            valor_right = self.right.obtener3D(ts)
            
            
            RETORNO.codigo += valor_left.codigo
            RETORNO.codigo += f'{self.left.etiquetaVerdadera}:\n'
            RETORNO.codigo += valor_right.codigo
            
            RETORNO.etiquetaV = self.etiquetaVerdadera
            RETORNO.etiquetaF = self.etiquetaFalsa
            RETORNO.tipo = Tipos.BOOLEAN
            
            return RETORNO
        
        
        if self.operador == Operador.OR:
            
            self.left.etiquetaVerdadera = self.etiquetaVerdadera
            self.left.etiquetaFalsa = ts.generador.obtenerEtiqueta()
            
            self.right.etiquetaVerdadera = self.etiquetaVerdadera
            self.right.etiquetaFalsa = self.etiquetaFalsa
            
            valor_left = self.left.obtener3D(ts)
            valor_right = self.right.obtener3D(ts)
            
            
            RETORNO.codigo += valor_left.codigo
            RETORNO.codigo += f'{self.left.etiquetaFalsa}:\n'
            RETORNO.codigo += valor_right.codigo
            
            RETORNO.etiquetaV = self.etiquetaVerdadera
            RETORNO.etiquetaF = self.etiquetaFalsa
            RETORNO.tipo = Tipos.BOOLEAN
            return RETORNO
        
        
        
        
  
    #    if tipo_left is not Tipos.BOOLEAN and tipo_right is not Tipos.BOOLEAN:
    #        pass
           
        
