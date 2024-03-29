
class Generador:
    
    temporal = 0
    etiqueta = 0
    codigo = []
    main = []
    funciones = []
    
    nativas = '''
    /* Nativas */
    void err_div_0(){
        printf("%c", (char)77) /*M*/; 
        printf("%c", (char)97); /*a*/
        printf("%c", (char)116); /*t*/
        printf("%c", (char)104); /*h*/
        printf("%c", (char)69);  /*E*/
        printf("%c", (char)114); /*r*/
        printf("%c", (char)114); /*r*/
        printf("%c", (char)111); /*o*/
        printf("%c", (char)114); /*r*/
        printf("%c", 10); 
    }
    
    void err_index_out_of_bounds(){
        printf("%c", 66); /*B*/
        printf("%c", 111); /*o*/
        printf("%c", 117); /*u*/
        printf("%c", 110); /*n*/
        printf("%c", 100); /*d*/
        printf("%c", 115); /*s*/
        printf("%c", 69); /*E*/
        printf("%c", 114); /*r*/
        printf("%c", 114); /*r*/
        printf("%c", 111); /*o*/
        printf("%c", 114); /*r*/
        printf("%c", 10); 
    }  
    '''
        
        
    def obtenerTemporal():
        temp = "t" + Generador.temporal.__str__()
        Generador.temporal += 1
        return temp
    
    def obtenerEtiqueta():
        etiq = "L" + Generador.etiqueta.__str__()
        Generador.etiqueta += 1
        return etiq
    
    def generarEncabezado() -> str:
        encabezado =[]
        encabezado.append("#include <stdio.h>")
        encabezado.append("float Stack[10000];")
        encabezado.append("float Heap[10000];")
        encabezado.append("int SP = 0;")
        encabezado.append("int HP = 0;")
        encabezado.append("\n")

        temp = []
        
        if Generador.temporal > 0:
            temp.append("float ")
        
        for i in range(0, Generador.temporal):
            temp.append(f't{i}')
            if i < Generador.temporal -1:
                temp.append(", ")
                
        if Generador.temporal > 0:
            temp.append(";")
            encabezado.append("".join(temp))
        
        return "\n".join(encabezado)
    
    
    def agregarInstruccion(codigo):
        Generador.main.append(codigo)
        
    def agregarFuncion(codigo):
        Generador.funciones.append(codigo)
        
    def generarCodigo() -> str:
        codigo_final = []
        codigo_final.append(Generador.generarEncabezado())
        
        # codigo = "\n".join(Generador.codigo)
        funciones = "\n".join(Generador.funciones)
        
        # codigo_final.append(codigo)
        # funciones.append(Generador.nativas)
        codigo_final.append(Generador.nativas)
        
        codigo_final.append(funciones)
        
        codigo_final.append("int main(){")
        main_c = "\n".join(Generador.main)
        codigo_final.append(main_c)
        codigo_final.append("   return 0;")
        codigo_final.append("}")
        
        return "\n".join(codigo_final)   
    
    def reiniciar():
        Generador.temporal = 0
        Generador.etiqueta = 0
        # Generador.codigo = []
        Generador.main = []
        Generador.funciones = []
             
        