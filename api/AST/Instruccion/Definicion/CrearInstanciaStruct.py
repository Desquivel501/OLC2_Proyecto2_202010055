

from Entorno.Simbolos.InstanciaStruct import InstanciaStruct
from Entorno.Simbolos.Struct import Struct
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion

from Entorno.TablaSimbolos import TablaSimbolos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador

class CrearInstanciaStruct(Instruccion):
    def __init__(self, id_instancia:str, instancia, mut:bool, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.instancia = instancia
        self.mut = mut
        self.linea = linea
        self.columna = columna
        
         
        
    def ejecutar3D(self, ts: TablaSimbolos):
        
        
        
        valor = self.instancia.obtener3D(ts)

        nueva_instancia = valor.valor
        
        struct:Struct = ts.obtenerStruct(nueva_instancia.id_struct)
        
        if struct is None:
            Error_("Semantico", f'Struct {struct.identificador} no ha sido declarado', ts.env, self.linea, self.columna)
            return ""
        
        
        # if nueva_instancia.id_struct != struct.identificador:
        #     Error_("Semantico", f'Intancia no es de tipo {struct.identificador}' , ts.env, self.linea, self.columna)
        
        nueva_instancia.id_instancia = self.id_instancia
        
        temp1 = Generador.obtenerTemporal()
        SALIDA = valor.codigo
        SALIDA += f'{temp1} = SP + {ts.tamanio};\n'
        ts.tamanio += 1
        SALIDA += f'Stack[(int){temp1}] = {valor.temporal};\n'
        SALIDA += f' /* FIN DECLARACION DE STRUCT */ \n\n'
        
        ts.agregarIntancia(self.id_instancia, nueva_instancia)
        
        return SALIDA
        
        
