from Entorno.Simbolos.InstanciaVector import InstanciaVector
from AST.Instruccion.Instruccion import Instruccion
from AST.misc.error import Error_
from Generador import Generador
from Entorno.Retorno import Retorno, Tipos
from AST.Expresion.Expresion import Expresion


class Remove(Instruccion, Expresion):
    
    def __init__(self, id_instancia, indice,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.indice = indice
        
    
    def ejecutar3D(self, ts):
        valor = self.obtener3D(ts)
        return valor.codigo
        
             
    def obtener3D(self, ts) -> Retorno:
        instancia = ts.buscar(self.id_instancia)
        
        if instancia is None:
            Error_('Semantico', f'Arreglo "{self.id_instancia}" no ha sido declarado', ts.env, self.linea, self.columna)  
            return Retorno()
    
        
        if not isinstance(instancia, InstanciaVector):
            Error_('Semantico', f'Simbolo "{self.id_instancia}" no es un vector', ts.env, self.linea, self.columna)  
            return Retorno() 
        
        indice = self.indice.obtener3D(ts)
        
        temp0 = Generador.obtenerTemporal()    
        temp1 = Generador.obtenerTemporal()    
        temp2 = Generador.obtenerTemporal()   
        temp3 = Generador.obtenerTemporal()   
        temp4 = Generador.obtenerTemporal()   
        temp5 = Generador.obtenerTemporal()
        temp6 = Generador.obtenerTemporal()  
        temp7 = Generador.obtenerTemporal()  
        temp8 = Generador.obtenerTemporal()  
        temp9 = Generador.obtenerTemporal()   
        
        loop = Generador.obtenerEtiqueta()
        etiqueta = Generador.obtenerEtiqueta()
        etiqueta2 = Generador.obtenerEtiqueta()
        
        SALIDA = "/* FUNCION REMOVE */\n"
        
        SALIDA += indice.codigo
        
        SALIDA += f'{temp0} = SP + {instancia.direccionRelativa};\n'
        
        SALIDA += f'{temp1} = Stack[(int) {temp0}];  /* Posicion del vector en el heap */  \n    '
        
        SALIDA += f'{temp2} = Heap[(int) {temp1}];  /* largo del vector */\n'
        
        SALIDA += f'{temp3} = {temp1} + 1;\n'
        SALIDA += f'{temp4} = Heap[(int) {temp3}];  /* Capacidad del vector */\n'
        
        SALIDA += f'{temp9} = 0;\n'
        
        # SALIDA += f' printf("%f ---- %f\\n", {indice.temporal},  {temp2});\n'
        
        SALIDA += f'if({temp2} == 0) goto {etiqueta};\n'
        SALIDA += f'if({indice.temporal} >= {temp2}) goto {etiqueta};\n'
        
        SALIDA += f'{temp3} = {temp3} + 1;\n'
        
        SALIDA += f'{temp3} = {temp3} + {indice.temporal};\n'
        SALIDA += f'{temp7} = {indice.temporal};\n'
        
        SALIDA += f'{temp9} = Heap[(int) {temp3}];\n'
    
        SALIDA += f'{loop}:\n'

        SALIDA += f'   {temp5} = {temp3} + 1;\n'

        SALIDA += f'    {temp6} = Heap[(int){temp5}];\n'
        SALIDA += f'    Heap[(int){temp3}] = {temp6};\n '
        
        SALIDA += f'    {temp3} = {temp3} + 1;\n'
        SALIDA += f'    {temp7} = {temp7} + 1;\n'
        
        SALIDA += f'if({temp7} < {temp2}) goto {loop};\n'
        
        SALIDA += f'    Heap[(int){temp3}] = 0;\n '
        
        SALIDA += f'{temp8} = {temp2} - 1;\n'
        SALIDA += f'Heap[(int) {temp1}] = {temp8};  /* Se cambia largo del vector */\n'
        SALIDA += f'goto {etiqueta2};'
        
        SALIDA += f'{etiqueta}:\n'
        SALIDA += f'err_index_out_of_bounds();'
        SALIDA += f'{temp9} = 0;'
        
        SALIDA += f'{etiqueta2}:\n'
        
        RETORNO = Retorno()
        RETORNO.iniciarRetorno(SALIDA,"", temp9, instancia.tipo_interno)
        
        return RETORNO