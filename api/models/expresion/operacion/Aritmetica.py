from cmath import sqrt
from models.expresion.Expresion import Expresion
from models.misc.error import Error_
from models.tabla.Tipos import Tipos, definirTipo
from models.expresion.operacion.Operacion import Operador, Operacion

class Aritmetica(Operacion):
    
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__(left, operador, right, linea, columna, unaria)
        
        self.linea = linea
        self.columna = columna
        self.tipo = None
    
    def getTipo(self, ts):
        if self.tipo == None:
            return definirTipo(self.getValor(ts))
        else:
            return self.tipo
    
    def getValor(self, ts):
        
        valor_left = self.left.getValor(ts)
        valor_right = self.right.getValor(ts) 
        
        tipo_left = self.left.getTipo(ts)
        tipo_right = self.right.getTipo(ts) 
        
        if self.unaria is True:
            return valor_left*(-1)
        
   
        if self.operador == Operador.POW:
            if tipo_left != Tipos.INT or tipo_right != Tipos.INT:
                raise Error_("Semantico",f'La operacion POW solo es valida con valores INT',ts.env, self.linea, self.columna)
            elif tipo_left == tipo_right:
                return valor_left ** valor_right
        
        if self.operador == Operador.POWF:
            if tipo_left != Tipos.FLOAT or tipo_right != Tipos.FLOAT:
                raise Error_("Semantico",f'La operacion POWF solo es valida con valores FLOAT',ts.env, self.linea, self.columna)
            elif tipo_left == tipo_right:
                return valor_left ** valor_right
            
        
        
        if self.operador == Operador.SUMA and tipo_left in [Tipos.STRING, Tipos.STR] and tipo_right in [Tipos.STR, Tipos.STRING] :
            self.tipo = tipo_left;
            return valor_left + valor_right
         
        
        if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
            raise Error_("Semantico",f'No se puede realizar una operacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
        
        if self.operador == Operador.SUMA:
            if tipo_left == tipo_right:
                return valor_left + valor_right
            else:
                raise Error_("Semantico",f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
                
        if self.operador == Operador.RESTA:
            if tipo_left == tipo_right:
                return valor_left - valor_right
            else:
                raise Error_("Semantico",f'No se puede realizar una resta entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
                
        if self.operador == Operador.MULTI:
            if tipo_left == tipo_right:
                return valor_left * valor_right
            else:
                raise Error_("Semantico",f'No se puede realizar una multiplicacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
                
        if self.operador == Operador.DIV:
            if valor_right == 0:
                 raise Error_("Semantico",f'La division entre 0 no esta definida',ts.env, self.linea, self.columna)
            elif tipo_left == tipo_right:
                return valor_left / valor_right
            else:
                raise Error_("Semantico",f'No se puede realizar una division entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
        
        if self.operador == Operador.MODULO:
            if tipo_left == tipo_right:
                return valor_left % valor_right
            else:
                raise Error_("Semantico",f'No se puede calcular el modulo entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
             
                
        if self.operador == Operador.ABS:
            return abs(valor_left)
        
        if self.operador == Operador.SQRT:
            if valor_left < 0:
                raise Error_("Semantico",f'La raiz cuadrada de negativos no esta definida',ts.env, self.linea, self.columna)
            else:
                return valor_left ** 0.5
            
        raise Error_("Semantico",f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)