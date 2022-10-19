

import copy
from struct import Struct
from Entorno.Simbolos.InstanciaArreglo import InstanciaArreglo
from Entorno.Simbolo import Simbolo
from AST.misc.error import Error_
from AST.Instruccion.Instruccion import Instruccion
from Entorno.Retorno import Tipos
from AST.Expresion.Expresion import Expresion
from Entorno.Retorno import Retorno, Tipos
from Generador import Generador
from Entorno.TablaSimbolos import TablaSimbolos
from AST.Instruccion.Definicion.Asignacion import Asignacion

class InstanciaStruct(Expresion):
    def __init__(self, id_struct, lista_atributos, linea, columna):
        self.id_struct = id_struct
        self.lista_atributos = lista_atributos
        self.id_instancia = None
        self.mut = None
        self.linea = linea
        self.columna = columna
        self.dic_atributos = {}
        self.compilada = False
        
        self.entorno = None

    
    def obtener3D(self, ts) -> Retorno:
        
        # copiaLista = copy.deepcopy(self.lista_atributos)
        RETORNO = Retorno()
        SALIDA = ""
        
        struct:Struct = ts.obtenerStruct(self.id_struct)
        
        if struct is None:
            Error_("Semantico", f'Struct {self.id_struct } no ha sido declarado', ts.env, self.linea, self.columna)
            return Retorno()
        
        temp1 = Generador.obtenerTemporal()
        
        SALIDA += f' /* DECLARACION DE STRUCT */ \n'
        SALIDA += f'{temp1} = HP; \n'
        SALIDA += f'HP = HP + {len(struct.campos)}; \n'
        
        ENTORNO = TablaSimbolos(ts, "Struct " + self.id_struct)
        self.entorno = ENTORNO
        # index = 0
        
        
        # for campo
        
        
        
        for campo in struct.campos:
            
            print(campo.identificador)
            
            if len(self.lista_atributos) == 0:
                Error_("Semantico", f'Numero incorrecto de atributos', ts.env, self.linea, self.columna)
                return Retorno()
            
            
            agregado = False
            
            i = 0
            for atributo in self.lista_atributos:
            
                if campo.identificador == atributo.identificador:

                    valor = atributo.valor.obtener3D(ts)
                    
                    # if isinstance(valor, InstanciaArreglo):
                    #     pass
                    
                    print(valor.tipo, '--' , campo.tipo)
                    
                    if valor.tipo == campo.tipo:
                        
                        asignacion = Asignacion(campo.identificador,None,valor.tipo, True, self.linea, self.columna)
                        asignacion.enStruct = True
                        asignacion.valorCompilado = valor
                        asignacion.puntero_nuevo = temp1    
                        SALIDA += asignacion.ejecutar3D(ts)

                        self.lista_atributos.pop(i)
                        agregado = True
                        break
                   
                    else:             
                        raise Error_("Semantico", f'Tipo incorrecto en atributo \'{campo.identificador}\'', ts.env, self.linea, self.columna)
                i += 1

            if not agregado:
                raise Error_("Semantico", f'No se encontro campo \'{campo.identificador}\' ', ts.env, self.linea, self.columna)
        
        if len(self.lista_atributos) != 0:
            raise Error_("Semantico", f'Atributos incorrectos', ts.env, self.linea, self.columna)
        

        
        RETORNO.iniciarRetornoInstancia(SALIDA, temp1, Tipos.STRUCT, self)
        
        return RETORNO



            