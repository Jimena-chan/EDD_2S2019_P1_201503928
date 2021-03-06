
import os
from graphviz import Digraph, nohtml
nickname = ""
class NodoDoble():
    def __init__(self, valor):
        self.sig = None
        self.ant = None
        self.valor = valor

class ListaDoble():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0
        self.nickname = ""
    
    def getSize(self):
        return self.size

    def getLista(self):
        return ll

    def setNickname(self, name):
        self.nickname = name 

    def getNickname(self):
        return self.nickname
        
    def getFinal(self):
        return self.fin.valor

    def eliminarCola(self):
        self.fin = self.fin.ant
        self.fin.sig = None
        self.size -= 1

    def estaVacia(self):
        return self.inicio is None

    def insertar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.estaVacia():
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.inicio.ant = nuevo
            nuevo.sig = self.inicio
            self.inicio = nuevo
        self.size += 1
    
    def eliminar(self, index):
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            if index >= 0 and index <= self.size:
                temp = self.inicio
                contar = 0
                if index == 0:
                        self.inicio = self.inicio.sig
                        self.inicio.ant = None
                        self.size -= 1
                else:
                    if index == self.size-1:
                        self.fin = self.fin.ant
                        self.fin.sig = None
                        self.size -= 1
                    while(temp.sig != None):   
                        if contar == index:
                            temp.sig.ant = temp.ant
                            temp.ant.sig = temp.sig
                            self.size -= 1
                        temp = temp.sig
                        contar += 1
                    
            else:
                print("Invalido")

    def obtener(self, index):
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            temp = self.inicio
            contar = 0
            while(temp != None):
                if index == contar:
                    print(temp.valor)
                temp = temp.sig
                contar +=1


    def graf2(self):      

        g = Digraph('ListaDoble', filename='grafica1.dot',  format='jpg' , node_attr={'shape': 'record', 'height': '.1'})
        temp = self.inicio
        g.graph_attr['rankdir'] = 'LR'
        while(temp != None): 
                       
            g.node(str(temp), nohtml('<f0> |<f1> '+str(temp.valor)+'|<f2>'))
            g.edge(str(temp),str(temp.sig))
            g.edge(str(temp),str(temp.ant))
            temp = temp.sig 
     
        g.save()
        os.system("dot grafica1.dot -o imagen1.jpg -Tjpg -Gcharset=utf8")
        

ll = ListaDoble()
val = ll.getNickname() 

