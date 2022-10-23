

from asyncore import loop
from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Simbolos.Funcion import Funcion
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from Entorno.Simbolo import Simbolo
from AST.Expresion.Expresion import Expresion
from Entorno.TablaSimbolos import TablaSimbolos
from Generador import Generador
from Entorno.Retorno import Retorno, Tipos

class Push(Instruccion):
    
    def __init__(self, id_instancia, expresion, linea, columna):
        self.expresion = expresion
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.tipo = None
        
             
    def ejecutar3D(self, ts):
        instancia = ts.buscar(self.id_instancia)
        
        if instancia is None:
            Error_('Semantico', f'Arreglo "{self.id_instancia}" no ha sido declarado', ts.env, self.linea, self.columna)  
            return Retorno()
    
        
        if not isinstance(instancia, InstanciaVector):
            Error_('Semantico', f'Simbolo "{self.id_instancia}" no es un vector', ts.env, self.linea, self.columna)  
            return Retorno()
        
        
        
        valor = self.expresion.obtener3D(ts)
        
        temp0 = Generador.obtenerTemporal()    
        temp1 = Generador.obtenerTemporal()    
        temp2 = Generador.obtenerTemporal()   
        temp3 = Generador.obtenerTemporal()   
        temp4 = Generador.obtenerTemporal()   
        temp5 = Generador.obtenerTemporal()  
        
        temp13 = Generador.obtenerTemporal()  
        
        temp6 = Generador.obtenerTemporal()  
        temp7 = Generador.obtenerTemporal()  
        temp8 = Generador.obtenerTemporal()  
        temp9 = Generador.obtenerTemporal() 
        temp10 = Generador.obtenerTemporal() 
        temp11 = Generador.obtenerTemporal()  
        temp12 = Generador.obtenerTemporal()    
        
        etiqueta = Generador.obtenerEtiqueta()
        etiqueta2 = Generador.obtenerEtiqueta()
        etiqueta3 = Generador.obtenerEtiqueta()
        loop = Generador.obtenerEtiqueta()
        
        
        SALIDA = "/* FUNCION PUSH */\n"
        
        SALIDA += valor.codigo
        
        SALIDA += f'{temp0} = SP + {instancia.direccionRelativa};\n'
        SALIDA += f'{temp1} = Stack[(int) {temp0}];  /* Posicion del vector en el heap */  \n    '
        
        SALIDA += f'{temp2} = Heap[(int) {temp1}];  /* largo del vector */\n'
        
        SALIDA += f'{temp3} = {temp1} + 1;\n'
        SALIDA += f'{temp4} = Heap[(int) {temp3}];  /* Capacidad del vector */\n'
        
        SALIDA += f'if({temp2} < {temp4}) goto {etiqueta};\n'
        SALIDA += "     /* EXPANDIR VECTOR */\n"
        
        SALIDA += f'     printf("here\\n");\n'
        
        SALIDA += f"    {temp5} = HP; /* Se obtiene posicion del Heap */ \n"
        SALIDA += f'    {temp6} = {temp2} + 3;\n'
        SALIDA += f'    HP = HP + {temp6};\n'
        
        SALIDA += f'    Heap[(int){temp5}] = {temp2} + 1; /* Nuevo tamaño del vector*/ \n'
        
        SALIDA += f'    {temp7} = {temp5} + 1; \n'
        SALIDA += f'    Heap[(int){temp7}] = {temp2} + 1; /*Nueva capacidad del vector*/ \n'
        
        SALIDA += f'    {temp13} = {temp5} + 1; \n'
        SALIDA += f'    {temp3} = {temp3} + 1;\n'
        
        SALIDA += f'    {temp8} = 0;\n'
        SALIDA += f'    {temp9} = {temp2};\n'
        
        SALIDA += f'    {loop}:'
        SALIDA += f'        {temp10} = {temp3} + {temp8};\n'
        SALIDA += f'        {temp11} = {temp13} + {temp8};\n'
        
        SALIDA += f'        {temp12} = Heap[(int){temp10}];\n'
        SALIDA += f'        Heap[(int){temp11}] = {temp12};\n '
        
        SALIDA += f'        {temp8} = {temp8} + 1;\n'
        SALIDA += f'    if({temp8} <= {temp2}) goto {loop};\n'
        
        SALIDA += f'    {temp8} = {temp8} + 1;\n'
        SALIDA += f'    {temp11} = {temp5} + {temp8};\n'
        SALIDA += f'    Heap[(int){temp11}] = {valor.temporal};\n '
        
        SALIDA += f'    {temp0} = SP + {instancia.direccionRelativa};\n'
        SALIDA += f'    Stack[(int) {temp0}] = {temp5};  /* Posicion del nuevo vector*/  \n    '
        
        SALIDA += f'    goto {etiqueta2};\n'
        
        # # SALIDA += 
        
        
        SALIDA += f'{etiqueta}:\n'
    
        SALIDA += f'    {temp3} = {temp1};\n'
        SALIDA += f'    {temp3} = {temp3} + 2;\n'
        SALIDA += f'    {temp3} = {temp3} + {temp2};\n'
        
        # SALIDA += f"       printf(\"%f\", (float){temp2});\n"
        
        SALIDA += f'    Heap[(int){temp3}] = {valor.temporal};\n '
        SALIDA += f'    Heap[(int){temp1}] = {temp2} + 1 ;  /* largo del vector */\n'
        
        # SALIDA += f"       printf(\"%f\", (float){temp2});\n"
        
        SALIDA += f'{etiqueta2}:\n'
        
        return SALIDA