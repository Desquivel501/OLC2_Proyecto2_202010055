from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion



class ArrayData(Expresion):

    def __init__(self, listaExpresiones, linea:int, columna: int):
        self.listaExpresiones = listaExpresiones
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, ts):
        return Tipos.ARRAY_DATA
    
    def getValor(self, ts):
        
        tipo = Tipos.VOID
        
        
        for i in range(0, len(self.listaExpresiones)):
            expresion = self.listaExpresiones[i]
            
            valor_expresion = expresion.getValor(ts)
            tipo_expresion = expresion.getTipo(ts)
            
            if i == 0:
                tipo = tipo_expresion
                self.expresionesCompiladas.append({"tipo":tipo_expresion, "valor":valor_expresion})
            
            else:
                if tipo != tipo_expresion:
                    raise Error_("Semantico", f'Tipos en arreglo no coinciden',   ts.env, self.linea, self.columna)
                else:
                    self.expresionesCompiladas.append({"tipo":tipo_expresion, "valor":valor_expresion})
                    
 
        
        self.listaDimensiones.append(len(self.expresionesCompiladas))
        
        
        tipoFin = Tipos.VOID
        
        for i in range(0, len(self.expresionesCompiladas)):
            
            expresionCompilada = self.expresionesCompiladas[i]
            
            valor_expresion = expresionCompilada.get("valor")
            tipo_expresion = expresionCompilada.get("tipo")
            
            if tipo_expresion != Tipos.ARRAY_DATA:
                tipoFin = tipo_expresion
                self.valores.append(valor_expresion)
                continue
            
            else:
                instanciaArray = valor_expresion
                if i == 0:
                    tipoFin = instanciaArray.tipo
                    self.listaDimensiones.extend(instanciaArray.dimensiones)
                
                else:
                    if instanciaArray.tipo != tipoFin:
                        raise Error_("Semantico", f'Tipos en arreglo no coinciden',   ts.env, self.linea, self.columna)
                
                self.valores.insert(i, instanciaArray.valores )
                
        
        
        instanciaArray = InstanciaArreglo(tipoFin, self.listaDimensiones, self.valores)
       
        return instanciaArray
        
        