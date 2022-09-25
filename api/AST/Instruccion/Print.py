from Entorno.Simbolos.InstanciaVector import InstanciaVector
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Retorno import Tipos
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion
from AST.Expresion.Expresion import Expresion
from AST.misc.Program import Program
from Entorno.Retorno import Retorno, Tipos, Tipos
from Entorno.TablaSimbolos import TablaSimbolos

class Print_(Instruccion):

    def __init__(self, valor: Expresion, list_exp, linea, columna):
        self.columna = columna
        self.linea = linea
        self.valor = valor
        self.list_exp = list_exp

    def ejecutar3D(self, ts: TablaSimbolos):
        salida = ""
        valor = self.valor.obtener3D(ts)
        
        #----------------------------------------------------------------INT
        print(valor.tipo)
        
        if valor.tipo == Tipos.INT:
            salida += "/* IMPRIMIR ENTERO */\n"
            salida += valor.codigo
            salida += f"printf(\"%d\\n\", (int){valor.temporal});\n"
            # ts.generador.agregarInstruccion(salida) 
           
        #----------------------------------------------------------------INT    
        if valor.tipo == Tipos.FLOAT:
            salida += "/* IMPRIMIR FLOAT */\n"
            salida += valor.codigo
            salida += f"printf(\"%f\\n\", (float){valor.temporal});\n"
            # ts.generador.agregarInstruccion(salida) 
            
        #----------------------------------------------------------------STRING O STR
        if valor.tipo in [Tipos.STRING, Tipos.STR]:
            temp = ts.generador.obtenerTemporal()
            caracter = ts.generador.obtenerTemporal()
            inicio = ts.generador.obtenerEtiqueta()
            fin = ts.generador.obtenerEtiqueta()

            salida += "/* IMPRIMIR CADENA */\n"
            salida += valor.codigo
            salida += f'{temp} = {valor.temporal};\n'
            salida += f'{inicio}:\n'
            salida += f'{caracter} = Heap[(int){temp}];\n'
            
            salida += f'if({caracter} == 0) goto {fin};\n'
            salida += f"    printf(\"%c\", (char){caracter});\n"
            salida += f'    {temp} = {temp} + 1;\n'
            salida += f'    goto {inicio};\n'
            salida += f'{fin}:\n'
            salida += f'    printf("\\n");\n'
            # ts.generador.agregarInstruccion(salida) 

        #----------------------------------------------------------------BOOLEAN    
        if valor.tipo == Tipos.BOOLEAN:
            etq_true = ts.generador.obtenerEtiqueta()
            etq_false = ts.generador.obtenerEtiqueta()
            
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
            # ts.generador.agregarInstruccion(salida) 
            
        return salida


