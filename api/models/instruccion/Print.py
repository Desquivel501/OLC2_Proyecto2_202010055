from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.expresion.Expresion import Expresion
from models.misc.Program import Program


class Print_(Instruccion):

    def __init__(self, cadena: Expresion, list_exp, linea, columna):
        self.columna = columna
        self.linea = linea
        self.cadena = cadena
        self.list_exp = list_exp

    def ejecutar(self, ts):
        
        cadena = str(self.cadena.getValor(ts))
        
        cadena = cadena.replace("\\n", "\n")
        
        if self.list_exp is not None:
            
            for exp in self.list_exp:
                
                valor = exp.getValor(ts)
                
                if  isinstance(valor, InstanciaArreglo):
                    valor = valor.valores
                    
                if  isinstance(valor, InstanciaVector):
                    valor = valor.valores
                
                x = cadena.find("{}")
                y = cadena.find('{:?}')
                
                
                if x == -1 and y == -1:
                    raise Error_("Semantico", "Numero incorrecto de parametros en Println!", ts.env, self.linea, self.columna)
                
                
                if x == -1 :
                    if not isinstance(valor, list):
                        raise Error_("Semantico", "Tipo incorrecto de parametros en Println!", ts.env, self.linea, self.columna)
                    cadena = cadena.replace("{:?}", str(valor),1)
                
                elif y == -1 :
                    if isinstance(valor, list):
                       raise Error_("Semantico", "Tipo incorrecto de parametros en Println!", ts.env, self.linea, self.columna)
                    cadena = cadena.replace("{}", str(valor),1)
                
                else:
                    if x < y:
                        if isinstance(valor, list):
                            raise Error_("Semantico", "Tipo incorrecto de parametros en Println!", ts.env, self.linea, self.columna)
                        cadena = cadena.replace("{}", str(valor),1)
                    
                    else:
                        if not isinstance(valor, list):
                            raise Error_("Semantico", "Tipo incorrecto de parametros en Println!", ts.env, self.linea, self.columna)
                        cadena = cadena.replace("{:?}", str(valor),1)
        
           
            
        x  = cadena.find("{}")
        y = cadena.find("{:?}")
        if x != -1 or y != -1:
            raise Error_("Semantico", "Numero incorrecto de parametros en Println!", ts.env, self.linea, self.columna)
            

            
        Program.console += cadena + "\n"