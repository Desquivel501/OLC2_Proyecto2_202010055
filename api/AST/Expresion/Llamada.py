

from Entorno.Retorno import Retorno, Tipos
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Generador import Generador

class Llamada(Expresion, Instruccion):
    
    def __init__(self, identificador: str, listaExpresiones, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        self.listaExpresiones = listaExpresiones
        

    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        SALIDA = ""
       
        funcion = ts.obtenerFuncion(self.identificador)
       
        if funcion is None:
           Error_("Semantico", f"Funcion {self.identificador} no ha sido declarada", ts.env, self.linea, self.columna)
           return Retorno()
        
        SALIDA += "/* LLAMADA A FUNCION */\n"
        
        ts_local = TablaSimbolos(ts, self.identificador)
        ts_local.tamanio = 1

        PUNTERO = Generador.obtenerTemporal()
        SALIDA += f'{PUNTERO} = SP + {ts.tamanio};\n'
        
        PARAMETROS = funcion.ejecutarParametros(ts_local, self.listaExpresiones, ts, PUNTERO)
        
        if not funcion.generada:
            funcion.generada = True
            codigo_funcion = funcion.ejecutar3D(ts_local)
            Generador.agregarFuncion(codigo_funcion)
            ts.agregarFuncion(funcion.identificador, funcion)


        SALIDA += PARAMETROS
        SALIDA += f'SP = SP + {ts.tamanio}; \n'
        SALIDA += f'{self.identificador}(); \n'
        SALIDA += f'SP = SP - {ts.tamanio}; \n'
        
        temp1 = Generador.obtenerTemporal()
        temp2 = Generador.obtenerTemporal()
        
        SALIDA += f'{temp1} = SP + {ts.tamanio}; \n'
        SALIDA += f'{temp2} = Stack[(int){temp1}]; \n'
        
        RETORNO = Retorno()
        
        RETORNO.iniciarRetorno(SALIDA,"", temp2, funcion.tipo)
        return RETORNO
    



    def ejecutar3D(self, ts: TablaSimbolos):
        res = self.obtener3D(ts)
        return res.codigo