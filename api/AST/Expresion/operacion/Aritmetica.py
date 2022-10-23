from ast import Return
from cmath import sqrt
from Entorno.Retorno import Retorno, Tipos
from AST.Expresion.Expresion import Expresion
from AST.misc.error import Error_

from AST.Expresion.operacion.Operacion import Operador, Operacion
from Entorno.TablaSimbolos import TablaSimbolos
from Generador import Generador

class Aritmetica(Operacion):
    
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__(left, operador, right, linea, columna, unaria)
    
    def obtener3D(self, ts: TablaSimbolos) -> Retorno:
               
        valor_left = self.left.obtener3D(ts)
        
        
        salida = ""
        retorno = Retorno()
        
        if self.unaria is True:
            temp = Generador.obtenerTemporal()
            salida += valor_left.codigo
            salida += f'{temp} = 0 - {valor_left.temporal};\n'
            retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
            return retorno
        
        if self.operador == Operador.ABS:
            salida += valor_left.codigo
            temp = Generador.obtenerTemporal()
            etq_false = Generador.obtenerEtiqueta()
            salida += f'if((int){valor_left.temporal} >= 0) goto {etq_false};\n'
            salida += f'    {valor_left.temporal} = 0 - {valor_left.temporal};\n'
            salida += f'{etq_false}:\n'
 
            retorno.iniciarRetorno(salida,"",valor_left.temporal,valor_left.tipo)
            return retorno
  
        valor_right = self.right.obtener3D(ts)
   
   
        if self.operador == Operador.POW:
            if valor_left.tipo != Tipos.INT or valor_right.tipo != Tipos.INT:
                Error_("Semantico",f'La operacion POW solo es valida con valores INT',ts.env, self.linea, self.columna)
            elif valor_left.tipo == valor_right.tipo:
                
                inicio = Generador.obtenerEtiqueta()
                fin = Generador.obtenerEtiqueta()
                temp = Generador.obtenerTemporal()
                temp2 = Generador.obtenerTemporal()
                salida += valor_left.codigo
                salida += valor_right.codigo
                
                salida += f'{temp} = {valor_left.temporal};\n'
                salida += f'{temp2} = {valor_right.temporal};\n'
                
                salida += f'{inicio}:\n' 
                salida += f'if({temp2} <= 0) goto {fin};\n'
                salida += f'    {temp} = {temp} * {valor_left.temporal};\n'
                salida += f'    {temp2} = {temp2} - 1;\n'
                salida += f'    goto {inicio};\n'
                salida += f'{fin}:\n'
                salida += f'    printf("\\n");\n'
                
                
                retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
                return retorno
            
        
        # if self.operador == Operador.POWF:
        #     if valor_left.tipo != Tipos.FLOAT or valor_right.tipo != Tipos.FLOAT:
        #         raise Error_("Semantico",f'La operacion POWF solo es valida con valores FLOAT',ts.env, self.linea, self.columna)
        #     elif valor_left.tipo == valor_right.tipo:
        #         return valor_left ** valor_right
            
        
        
        # if self.operador == Operador.SUMA and valor_left.tipo in [Tipos.STRING, Tipos.STR] and valor_right.tipo in [Tipos.STR, Tipos.STRING] :
        #     self.tipo = valor_left.tipo;
        #     return valor_left + valor_right
         
        
        # if valor_left.tipo not in [Tipos.INT, Tipos.FLOAT] and valor_right.tipo not in [Tipos.INT, Tipos.FLOAT]:
        #     Error_("Semantico",f'No se puede realizar una operacion entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
        
        
        # if self.operador == Operador.SUMA and tipo_left in [Tipos.STRING, Tipos.STR] and tipo_right in [Tipos.STR, Tipos.STRING] :
        #     self.tipo = tipo_left;
        #     return valor_left + valor_right
        
        
        if self.operador == Operador.SUMA:
            
            if valor_left.tipo in [Tipos.STRING, Tipos.STR] and valor_right.tipo in [Tipos.STRING, Tipos.STR]:

                return self.concatenar(ts, valor_left, valor_right)
                
            
            
            if valor_left.tipo == valor_right.tipo:
                salida += valor_left.codigo
                salida += valor_right.codigo
                temp = Generador.obtenerTemporal()
                salida += f'{temp} = {valor_left.temporal} + {valor_right.temporal};\n'
                retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
                return retorno

            # elif valor.
            
            else:
                Error_("Semantico",f'No se puede realizar una suma entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
                return Retorno()
        
        
        if valor_left.tipo not in [Tipos.INT, Tipos.FLOAT] or valor_right.tipo not in [Tipos.INT, Tipos.FLOAT]:
            Error_("Semantico",f'No se puede realizar una suma entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
            return Retorno()
             
                
        if self.operador == Operador.RESTA:
            if valor_left.tipo == valor_right.tipo:
                salida += valor_left.codigo
                salida += valor_right.codigo
                temp = Generador.obtenerTemporal()
                salida += f'{temp} = {valor_left.temporal} - {valor_right.temporal};\n'
                retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
                return retorno
            else:
                Error_("Semantico",f'No se puede realizar una resta entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
                return Retorno()
                
        if self.operador == Operador.MULTI:
            if valor_left.tipo == valor_right.tipo:
                salida += valor_left.codigo
                salida += valor_right.codigo
                temp = Generador.obtenerTemporal()
                salida += f'{temp} = {valor_left.temporal} * {valor_right.temporal};\n'
                retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
                return retorno
            else:
                Error_("Semantico",f'No se puede realizar una multiplicacion entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
                return Retorno()
                
        if self.operador == Operador.DIV:
            if valor_left.tipo == valor_right.tipo:
                salida += valor_left.codigo
                salida += valor_right.codigo
                temp = Generador.obtenerTemporal()
                etq_1 = Generador.obtenerEtiqueta()
                etq_2 = Generador.obtenerEtiqueta()

                salida += f'{temp} = 0;\n'
                salida += f'if({valor_right.temporal} == 0) goto {etq_1};\n'
                salida += f'{temp} = {valor_left.temporal} / {valor_right.temporal};\n'
                salida += f'goto {etq_2};\n'
                
                salida += f'{etq_1}:\n'
                salida += f'err_div_0();\n'
                salida += f'{etq_2}:\n'
                
                
                retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
                return retorno
            else:
                Error_("Semantico",f'No se puede realizar una division entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
                return Retorno()
        
        if self.operador == Operador.MODULO:
            if valor_left.tipo == valor_right.tipo:
                salida += valor_left.codigo
                salida += valor_right.codigo
                temp = Generador.obtenerTemporal()
                salida += f'{temp} = (int){valor_left.temporal} % (int){valor_right.temporal};\n'
                retorno.iniciarRetorno(salida,"",temp,valor_left.tipo)
                return retorno
            else:
                Error_("Semantico",f'No se puede calcular el modulo entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
                return Retorno()
             
                
        

        
        if self.operador == Operador.SQRT:
 
                error = Generador.obtenerTemporal()
                inicio = Generador.obtenerEtiqueta()
                fin = Generador.obtenerEtiqueta()        
                
                cond = Generador.obtenerTemporal()
                temp1 = Generador.obtenerTemporal()
                temp2 = Generador.obtenerTemporal()
                temp3 = Generador.obtenerTemporal()
                res = Generador.obtenerTemporal()

                salida += valor_left.codigo
                
                salida += "/* RAIZ CUADRADA */\n"
                
                salida += f'{res} = {valor_left.temporal}; \n'
                salida += f'{error} = 0.00001; \n'
                
                salida += f'{inicio}: \n'
                
                salida += f'{temp1} = {valor_left.temporal} / {res}; \n'
                salida += f'{cond} = {res} - {temp1}; \n'
                
                salida += f'if((float){cond} <= {error}) goto {fin};\n'
                salida += f'    {temp2} = {valor_left.temporal} / {res}; \n'
                salida += f'    {temp3} = {res} + {temp2}; \n'
                salida += f'    {res} = {temp3} / 2; \n'
                salida += f'goto {inicio};\n'
    
                salida += f'{fin}: \n'
                

                #-----------EXPLICACION RAIZ
                # Raiz cuadrada con algoritmo babilonico
                # error = 0.00001;  // Este es el error de la operacion
                # s = numero;
                # while ((s - numero / s) > error): // Se repite el ciclo hasta que se llega a la presicion deseada
                #     s = (s + numero / s) / 2;
                # return s;  // 's' contendra la raiz cuadrada de 'numero'                       
                                
                
                retorno.iniciarRetorno(salida,"",res,Tipos.FLOAT)
                return retorno
            
            
        Error_("Semantico",f'No se puede realizar una operacion entre {Tipos(valor_left.tipo).name} y {Tipos(valor_right.tipo).name}',ts.env, self.linea, self.columna)
        return Retorno()
    
    
    def concatenar(self, ts, left, right):
        
        RETORNO = Retorno()
        SALIDA = "/* CONCATENAR */\n"
        
        SALIDA += left.codigo
        SALIDA += right.codigo
        
        temp = Generador.obtenerTemporal()
        temp2 = Generador.obtenerTemporal()
        caracter = Generador.obtenerTemporal()
        
        inicio1 = Generador.obtenerEtiqueta()
        inicio2 = Generador.obtenerEtiqueta()
        salida1 = Generador.obtenerEtiqueta()
        salida2 = Generador.obtenerEtiqueta()
        
        
        SALIDA += f'{temp2} = HP; \n'
        SALIDA += f'{temp} = {left.temporal}; \n'
           
        SALIDA += f'{inicio1}:\n'    
        SALIDA += f'{caracter} = Heap[(int){temp}];\n'
        SALIDA += f'if({caracter} == 0) goto {salida1};\n'
        SALIDA += f'Heap[HP] = {caracter};\n'
        SALIDA += f'HP = HP + 1; \n'
        SALIDA += f'{temp} = {temp} + 1; \n'
        SALIDA += f'goto {inicio1};\n'
        SALIDA += f'{salida1}:\n'

        SALIDA += f'{temp} = {right.temporal}; /*here*/ \n'
        
        SALIDA += f'{inicio2}:\n'    
        SALIDA += f'{caracter} = Heap[(int){temp}];\n'
        SALIDA += f'if({caracter} == 0) goto {salida2};\n'
        SALIDA += f'Heap[HP] = {caracter};\n'
        SALIDA += f'HP = HP + 1; \n'
        SALIDA += f'{temp} = {temp} + 1; \n'
        SALIDA += f'goto {inicio2};\n'
        SALIDA += f'{salida2}:\n'

        SALIDA += f'Heap[HP] = 0; \n'
        SALIDA += f'HP = HP + 1; \n'
        SALIDA += f'Heap[HP] = 0; \n'
        SALIDA += f'HP = HP + 1; \n'
        
        RETORNO.iniciarRetorno(SALIDA, "", temp2, Tipos.STRING)
        
        return RETORNO