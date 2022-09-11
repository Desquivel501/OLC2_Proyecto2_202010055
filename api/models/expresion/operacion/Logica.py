from models.misc.error import Error_
from models.tabla.Tipos import Tipos, definirTipo
from models.expresion.operacion.Operacion import Operador, Operacion

class Logica(Operacion):
    
    def getTipo(self, ts):
        return definirTipo(self.getValor(ts))
    
    def getValor(self, ts):
        valor_left = self.left.getValor(ts)
        valor_right = self.right.getValor(ts)
        
        tipo_left = self.left.getTipo(ts)
        tipo_right = self.right.getTipo(ts) 
        
        if self.operador == Operador.NOT:
            if tipo_left is not Tipos.BOOLEAN and tipo_right is not Tipos.BOOLEAN:
                raise Error_("Semantico",f'No se puede negar un valor tipo {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
            return not valor_left

        if tipo_left is not Tipos.BOOLEAN and tipo_right is not Tipos.BOOLEAN:
                raise Error_("Semantico",f'No se puede realizar operacion logica entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',ts.env, self.linea, self.columna)
        
        if self.operador == Operador.AND:
            return valor_left and valor_right
             
        if self.operador == Operador.OR:
            return valor_left or valor_right
           
        
