from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import json
from AST.misc.Program import Program

from Entorno.TablaSimbolos import TablaSimbolos
from AST.ast import Ast
from Generador import Generador

from Analizador.parser import parser
from Entorno.Simbolos.Funcion import Funcion
from AST.misc.error import Error_

app = Flask(__name__)
CORS(app)

Generador3D = Generador()

# ast: Ast = parser.parse("ejecutar(1 + 1); ejecutar(1 + 1);")

# ts = TablaSimbolos(None, 'Global')
# driver = Driver()
# ast.ejecutar(driver, ts)

# print(driver.console)
@app.route("/simbolos",methods=["GET"])
def tabla_simbolos():
    if request.method == 'GET':
        return  json.dumps(Program.tabla, indent=2)
    

@app.route("/errores",methods=["GET"])
def tabla_errores():
    if request.method == 'GET':
        return  json.dumps(Program.errores, indent=2)
    
@app.route("/tablas",methods=["GET"])
def tabla_tablas():
    if request.method == 'GET':
        return  json.dumps(Program.lista_tablas, indent=2)

@app.route("/bases",methods=["GET"])
def tabla_bases():
    if request.method == 'GET':
        return  json.dumps(Program.lista_bases, indent=2)
    
    
@app.route("/interpretar",methods=["POST"])
def interpretar():
    
    # generador = Generador()
    
    Generador.reiniciar()

    if request.method == 'POST':
        Program.console = ""
        Program.tabla = []
        Program.errores = []
        data = request.json

        instrucciones = data.get('instrucciones')
        
        if instrucciones != "":
            
            if len(Program.errores) <= 0:

                ast: Ast = parser.parse(instrucciones)
                ts = TablaSimbolos(None, 'Main')

                for instruccion in ast.instrucciones:
                    
                    if isinstance(instruccion, Funcion):
                        instruccion.ejecutarFuncion(ts)
            
            
                main = ts.obtenerFuncion("main")
                if main is not None:
                    codigo = main.instrucciones.codigo
                    
                    for intr in codigo:
                        Generador.agregarInstruccion(intr.ejecutar3D(ts)) 
  
            
                

    return {
        'resultado': Generador.generarCodigo()
    }


if __name__ == "__main__":
    app.run(threaded=True, debug=True, port=5000)