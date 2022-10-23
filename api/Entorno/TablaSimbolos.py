# from Entorno.Simbolos.Modulo import Modulo

from Entorno.Retorno import Tipos
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
# from Entorno.Simbolos.Funcion import Funcion
from AST.misc.Program import Program
from Entorno.Simbolo import Simbolo
from Generador import Generador

class TablaSimbolos:

    def __init__(self, anterior, env):
        self.env = env
        self.anterior = anterior
        self.tabla = {}
        self.variables = {}
        self.funciones = {}
        self.structs = {}
        self.instancias_structs = {}
        self.arreglos = {}
        self.vectores = {}
        self.modulos = {}
        
        # self.generador = generador
        self.tamanio = 0
        self.Display = [0] * 1000
        self.ptr = 0

    def add(self, id: str, simbolo: Simbolo, linea, columna):
                
        self.tabla[id] = simbolo
        tipo = self.getTiposNombre(simbolo.tipo)
        Program.tabla.append({"id":id, "tipo":tipo, "ambito":self.env, "linea": linea, "columna": columna})

    def buscar(self, id: str) -> Simbolo:
        ts = self

        while ts is not None:
            exist = ts.tabla.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None


    def buscarActual(self, id: str) -> Simbolo:
        return self.tabla.get(id)


    def getGlobal(self):
        env = self
        while env.anterior is not None:
            env = env.anterior
        return env

    #-------------------------------------------FUNCIONES-----------------------------------------------

    def agregarFuncion(self, id: str,  func):
        self.funciones[id] = func


    def obtenerFuncion(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.funciones.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

     #-------------------------------------------STRUCTS-----------------------------------------------

    def agregarStruct(self, id: str,  struct):
        self.structs[id] = struct


    def obtenerStruct(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.structs.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def obtenerInstancia(self, id:str):
        ts = self
        while ts is not None:
            exist = ts.instancias_structs.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def agregarIntancia(self, id: str,  struct):
        self.instancias_structs[id] = struct


    #-------------------------------------------ARREGLOS-----------------------------------------------

    def agregarArreglo(self, id: str,  arreglo: InstanciaArreglo):
        self.arreglos[id] = arreglo


    def obtenerArreglo(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.arreglos.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

        #-----------------------------------------VECTORES-----------------------------------------------

    def agregarVector(self, id: str,  vector):
        self.vectores[id] = vector


    def obtenerVector(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.vectores.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None
    

#-------------------------------------------MODULOS-----------------------------------------------

    def agregarModulo(self, id: str,  mod):
        self.modulos[id] = mod


    def obtenerModulo(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.modulos.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None
    
    def nuevoEntornoMod(self, identificador):
        ts_modulo = TablaSimbolos(self, identificador)
        return ts_modulo


#-------------------------------------------TIPOS REPORTE-----------------------------------------------

    def getTiposNombre(self, s):
        
        
        if s == Tipos.INT:
            return "i64"
        if s == Tipos.FLOAT:
            return "f64"
        if s == Tipos.BOOLEAN:
            return "bool"
        if s == Tipos.STR:
            return "&str"
        if s == Tipos.STRING:
            return "String"
        if s == Tipos.CHAR:
            return "Char"
        if s == Tipos.ARRAY_DATA:
            return "Arreglo"
        if s == Tipos.VECTOR_DATA:
            return "Vector"
        if s == Tipos.STRUCT:
            return "Struct"
        else:
            return ""
            


    