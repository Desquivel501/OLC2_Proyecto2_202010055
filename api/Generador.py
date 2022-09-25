
class Generador:
    
    def __init__(self) -> None:
        self.temporal = 0
        self.etiqueta = 0
        self.codigo = []
        self.main = []
        
    def obtenerTemporal(self):
        temp = "t" + self.temporal.__str__()
        self.temporal += 1
        return temp
    
    def obtenerEtiqueta(self):
        etiqueta = "L" + self.etiqueta.__str__()
        self.etiqueta += 1
        return etiqueta
    
    def generarEncabezado(self) -> str:
        encabezado =[]
        encabezado.append("#include <stdio.h>")
        encabezado.append("float Stack[10000];")
        encabezado.append("float Heap[10000];")
        encabezado.append("int SP = 0;")
        encabezado.append("int HP = 0;")
        encabezado.append("\n")

        temp = []
        
        if self.temporal > 0:
            temp.append("float ")
        
        for i in range(0, self.temporal):
            temp.append(f't{i}')
            if i < self.temporal -1:
                temp.append(", ")
                
        if self.temporal > 0:
            temp.append(";")
            encabezado.append("".join(temp))
        
        return "\n".join(encabezado)
    
    
    def agregarInstruccion(self, codigo):
        self.main.append(codigo)
        
    def generarCodigo(self) -> str:
        codigo_final = []
        codigo_final.append(self.generarEncabezado())
        
        codigo = "\n".join(self.codigo)
        codigo_final.append(codigo)
        codigo_final.append("int main(){")
        
        main = "\n".join(self.main)
        codigo_final.append(main)
        codigo_final.append("   return 0;")
        codigo_final.append("}")
        
        return "\n".join(codigo_final)   
    
    def reiniciar(self):
        self.temporal = 0
        self.etiqueta = 0
        self.codigo = []
        self.main = []
             
        