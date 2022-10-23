
from tkinter.messagebox import RETRY
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Entorno.Retorno import Retorno, Tipos
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Generador import Generador
from AST.Expresion.Acceso.AccesoVector import AccesoVector
from Entorno.Simbolos.InstanciaVector import InstanciaVector

class AccesoArreglo(Expresion):
    
    def __init__(self, id_instancia, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna

             
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
        
        instancia = ts.buscar(self.id_instancia)
        
        if instancia is None:
            Error_('Semantico', f'Arreglo "{self.id_instancia}" no ha sido declarado', ts.env, self.linea, self.columna)  
            return Retorno()
        
        if isinstance(instancia, InstanciaVector):
            vector = AccesoVector(instancia,self.listaExpresiones,self.linea,self.columna)
            return vector.obtener3D(ts)
        
        if not isinstance(instancia, InstanciaArreglo):
            Error_('Semantico', f'Simbolo "{self.id_instancia}" no es un arreglo', ts.env, self.linea, self.columna)  
            return Retorno()

        
        temp1 = Generador.obtenerTemporal()    
        temp2 = Generador.obtenerTemporal()   
        etiqueta = Generador.obtenerEtiqueta()
        
        SALIDA = "/* Acceso Arreglo */\n"
        SALIDA += f'{temp1} = SP + {instancia.direccionRelativa};\n'
        SALIDA += f'{temp2} = Stack[(int) {temp1}];\n'
        
        
        dimensiones_compiladas = self.compilarDimensiones(ts)
        if dimensiones_compiladas is None:
            return Retorno()
        
        for exp in dimensiones_compiladas:
            SALIDA += exp.codigo
        
        
        if len(self.listaExpresiones) != len(dimensiones_compiladas):
            Error_('Semantico', f'Dimensiones Incorrectas', ts.env, self.linea, self.columna)  
            return Retorno()
    
        RESULTADO = self.acceso(ts, dimensiones_compiladas, temp2)
        
        RESULTADO.tipo = instancia.tipo_interno
    
        if( len(instancia.dimensiones) > len(self.listaExpresiones) ):
            RESULTADO.tipo = Tipos.ARRAY_DATA
            
        SALIDA += RESULTADO.codigo
        SALIDA = SALIDA.replace("SALIR_ARREGLO", etiqueta)
        SALIDA += f'{etiqueta}:\n'
        
        
        RETORNO = Retorno()
        
        RETORNO.tipo_interno = instancia.tipo_interno
        RETORNO.iniciarRetorno(SALIDA, "", RESULTADO.temporal, RESULTADO.tipo)
        
        return RETORNO
    
    
    def compilarDimensiones(self, ts):  
        dimensiones_compiladas = []
        
        for exp in self.listaExpresiones:
            valor = exp.obtener3D(ts) 
            if valor.tipo is not Tipos.INT:
                Error_('Semantico', f'Dimension de un arreglo debe de ser de tipo i64', ts.env, self.linea, self.columna)   
                return None
            
            dimensiones_compiladas.append(valor)
        return dimensiones_compiladas
    
    
    def acceso(self, ts, lista_expresiones, temporal):
        
        SALIDA = "/* Accediendo */\n"
        
        expresion = lista_expresiones.pop(0)
        
        temp1 = Generador.obtenerTemporal()
        temp2 = Generador.obtenerTemporal()
        temp3 = Generador.obtenerTemporal()
        temp4 = Generador.obtenerTemporal()
        
        SALIDA += f'{temp1} = Heap[(int) {temporal}]; /* Se obtiene el tamaño del arreglo */\n'
        SALIDA += f'if ({expresion.temporal} > {temp1}) goto SALIR_ARREGLO; \n'
        SALIDA += f'{temp2} = {temporal} + 1; \n'
        SALIDA += f'{temp3} = {temp2} + {expresion.temporal}; \n'
        SALIDA += f'{temp4} = Heap[(int) {temp3}]; \n'
        
        RETORNO = Retorno()
        
        if(len(lista_expresiones) > 0):
            res = self.acceso(ts, lista_expresiones, temp4)
            SALIDA += res.codigo
            RETORNO.iniciarRetorno(SALIDA, "", res.temporal, None)
        else:
            RETORNO.iniciarRetorno(SALIDA, "", temp4, None)
        
        return RETORNO