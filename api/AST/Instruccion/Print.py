from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from AST.misc.Program import Program
from Entorno.Retorno import Retorno, Tipos, Tipos
from Entorno.TablaSimbolos import TablaSimbolos
from Generador import Generador

class Print_(Instruccion):

    def __init__(self, valor: Expresion, list_exp, linea, columna):
        self.columna = columna
        self.linea = linea
        self.valor = valor
        self.list_exp = list_exp

    def ejecutar3D(self, ts: TablaSimbolos):
        salida = ""
        valor = self.valor.obtener3D(ts)
        
        # print(valor.tipo)
        
        #----------------------------------------------------------------INT
    
        if valor.tipo == Tipos.INT:
            salida += "/* IMPRIMIR ENTERO */\n"
            salida += valor.codigo
            salida += f"printf(\"%d\\n\", (int){valor.temporal});\n"
            # Generador.agregarInstruccion(salida) 
           
        #----------------------------------------------------------------INT    
        if valor.tipo == Tipos.FLOAT:
            salida += "/* IMPRIMIR FLOAT */\n"
            salida += valor.codigo
            salida += f"printf(\"%f\\n\", (float){valor.temporal});\n"
            # Generador.agregarInstruccion(salida) 
            
        #----------------------------------------------------------------STRING O STR
        if valor.tipo in [Tipos.STRING, Tipos.STR]:
            salida += self.printString(salida, valor)
            # salida += f'    printf("\\n");\n'
            # Generador.agregarInstruccion(salida) 

        #----------------------------------------------------------------BOOLEAN    
        if valor.tipo == Tipos.BOOLEAN:
            etq_true = Generador.obtenerEtiqueta()
            etq_false = Generador.obtenerEtiqueta()
            
            salida += "/* IMPRIMIR BOOLEAN */\n"
            salida += valor.codigo
            
            salida += f'if((int){valor.temporal} == 0) goto {etq_false};\n'
            salida += f"    printf(\"%c\", (char)116);\n"
            salida += f"    printf(\"%c\", (char)114);\n"
            salida += f"    printf(\"%c\", (char)117);\n"
            salida += f"    printf(\"%c\", (char)101);\n"
            salida += f'    goto {etq_true};\n'
            salida += f'{etq_false}:\n'
            salida += f"    printf(\"%c\", (char)102);\n"
            salida += f"    printf(\"%c\", (char)97);\n"
            salida += f"    printf(\"%c\", (char)108);\n"
            salida += f"    printf(\"%c\", (char)115);\n"
            salida += f"    printf(\"%c\", (char)101);\n"
            salida += f'{etq_true}:\n'
            salida += f'    printf("\\n");\n'
            # Generador.agregarInstruccion(salida) 
        
        #-------------------------------------------------------------------ARRAY DATA
        if valor.tipo == Tipos.ARRAY_DATA:
            
            salida = self.printArreglo(valor)

        return salida
    
    
    def printString(self, salida, valor):
        temp = Generador.obtenerTemporal()
        caracter = Generador.obtenerTemporal()
        inicio = Generador.obtenerEtiqueta()
        fin = Generador.obtenerEtiqueta()

        salida += "/* IMPRIMIR CADENA */\n"
        salida += valor.codigo
        salida += f'{temp} = {valor.temporal};\n'
        salida += f'{inicio}:\n'
        salida += f'{caracter} = Heap[(int){temp}];\n'
            
        salida += f'if({caracter} == 0) goto {fin};\n'
        salida += f"    printf(\"%c\", (char){caracter}); \n"
        salida += f'    {temp} = {temp} + 1;\n'
        salida += f'    goto {inicio};\n'
        salida += f'{fin}:\n'
        salida += f'    printf("\\n");\n'
        
        return salida

    
    def printStringArray(self, temporal):
        # temp = Generador.obtenerTemporal()
        caracter = Generador.obtenerTemporal()
        inicio = Generador.obtenerEtiqueta()
        fin = Generador.obtenerEtiqueta()

        salida = "/* IMPRIMIR CADENA */\n"
        salida += f'{inicio}:\n'
        salida += f'{caracter} = Heap[(int){temporal}];\n'
            
        salida += f'if({caracter} == 0) goto {fin};\n'
        salida += f"    printf(\"%c\", (char){caracter}); \n"
        salida += f'    {temporal} = {temporal} + 1;\n'
        salida += f'    goto {inicio};\n'
        salida += f'{fin}:\n'        
        return salida



    def printArreglo(self, valor):
        
        salida = ""
        
        etq_loop = Generador.obtenerEtiqueta()
        etq_salir = Generador.obtenerEtiqueta()
        limite = Generador.obtenerTemporal()
        contador = Generador.obtenerTemporal()
        caracter = Generador.obtenerTemporal()
        temp = Generador.obtenerTemporal()
            
        salida += "/* IMPRIMIR ARRAY */\n"
        salida += valor.codigo
        salida += f'{limite} = Heap[(int) {valor.temporal}];\n'
        salida += f'{limite} = {limite} + 1;\n'
        salida += f'{contador} = 1;\n'
            
            # salida += f"printf(\"%d\\n\", (int){limite});\n"
        
        salida += "/* IMPRIMIR CONTENIDO */\n" 
        salida += f"printf(\"%c\", (char)91);\n"
            
        salida += f'{etq_loop}:\n'
            
        salida += f'{temp} = {valor.temporal} + {contador} ;\n'
            
        salida += f'{caracter} =  Heap[(int) {temp}];\n'
            
            
        print(valor.tipo_interno)
            
        if (valor.tipo_interno == Tipos.INT):
            salida += f"printf(\"%d\", (int){caracter});\n"
                
        if (valor.tipo_interno == Tipos.FLOAT):
            salida += f"printf(\"%f\", (float){caracter});\n"
            
        if (valor.tipo_interno in [Tipos.STRING, Tipos.STR]):
            salida += self.printStringArray(caracter)
        
        
        # salida += f"printf(\"%d\", (int){caracter});\n"
            
        salida += f'{contador} = {contador} + 1;\n'
            
        salida += f'if((int){contador} == (int){limite}) goto {etq_salir};\n'
            
        salida += f"printf(\"%c\", (char)44);\n"
            
        salida += f'goto {etq_loop};\n'
            
        salida += f'{etq_salir}:\n'
            
        salida += f"printf(\"%c\\n\", (char)93);\n"
        
        
        
        return salida
    
