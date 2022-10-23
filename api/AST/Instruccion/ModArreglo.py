
from Entorno.Retorno import Retorno, Tipos
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion

from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Generador import Generador

class ModArreglo(Instruccion):
    
    def __init__(self, id_instancia, listaExpresiones, expresion ,linea, columna):
        self.listaExpresiones = listaExpresiones
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.tipo = None
        self.expresion = expresion
        
             
    def ejecutar3D(self, ts):
        instancia = ts.buscar(self.id_instancia)
        
        if instancia is None:
            Error_('Semantico', f'Arreglo "{self.id_instancia}" no ha sido declarado', ts.env, self.linea, self.columna)  
            return Retorno()
        
        # if isinstance(instancia, InstanciaVector):
        #     vector = ModVector(instancia,self.listaExpresiones, self.expresion, self.linea,self.columna)
        #     return vector.obtener3D(ts)
        
        if not isinstance(instancia, InstanciaArreglo):
            Error_('Semantico', f'Simbolo "{self.id_instancia}" no es un arreglo', ts.env, self.linea, self.columna)  
            return Retorno()

        
        valor = self.expresion.obtener3D(ts)
        
        temp1 = Generador.obtenerTemporal()    
        temp2 = Generador.obtenerTemporal()   
        etiqueta = Generador.obtenerEtiqueta()
        
        SALIDA = "/* Modificar Arreglo */\n"
        
        SALIDA += valor.codigo
        
        SALIDA += f'{temp1} = SP + {instancia.direccionRelativa};\n'
        SALIDA += f'{temp2} = Stack[(int) {temp1}];\n'
        
        
        dimensiones_compiladas = self.compilarDimensiones(ts)
        if dimensiones_compiladas is None:
            return ""
        
        for exp in dimensiones_compiladas:
            SALIDA += exp.codigo

        
        if len(self.listaExpresiones) != len(dimensiones_compiladas):
            Error_('Semantico', f'Dimensiones Incorrectas', ts.env, self.linea, self.columna)  
            return ""
        
        
        RESULTADO = self.acceso(ts, dimensiones_compiladas, temp2)
        
        SALIDA += RESULTADO.codigo
        
        SALIDA += f'Heap[(int) {RESULTADO.temporal}] = {valor.temporal}; \n'
        
        SALIDA = SALIDA.replace("SALIR_ARREGLO", etiqueta)
        SALIDA += f'{etiqueta}:\n'
        

        return SALIDA
    
    
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
            RETORNO.iniciarRetorno(SALIDA, "", temp3, None)
        
        return RETORNO