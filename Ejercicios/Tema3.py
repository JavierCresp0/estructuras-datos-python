# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:22:04 2025

@author: Usuario
"""

### Insertar paga 24 tema 3

"""
Tipo nodo
 {
 

 }
 
Insertas al final funcion:

1. Crear un nuevo nodo
    nuevoNodo.X <-- T
    nuevoNodo.Y <-- T
    nuevoNodo.Siguiente <-- None
    
2. Si la lista esta vacia (lista,Cabeza = NUlO)
    lista.Cabeza = nuevoNodo
    fin

3. Actual <-- lista.cabeza
    While Actual.Siguiente != NULO
        Actual <-- Actual.Siguiente
    FIN WHILE
    
    Actual.Siguiente <-- nuevoNodo
"""

#MEmoria dinamica

class Nodo:
    
    def __init__(self,Y,X):
        self.X = X
        self.Y = Y
        self.Siguiente = None

class Lista:
    
    def __init__(self):
        self.Cabeza = None
        self.Ultimo = None
        
    def insertarFinal(self,X,Y):
        
        nuevoNodo = Nodo(Y, X)
        
        if self.Cabeza == None:
            self.Cabeza = nuevoNodo
            self.Ultimo = nuevoNodo
            return 
        else:            
            ultimo= self.Ultimo
            ultimo.Siguiente = nuevoNodo
            self.Ultimo = nuevoNodo
            
    def elimininarPrimeroa(self):
        
        if self.Cabeza == None:
            print("no hay elementos")
        else:
            nodoEliminar = self.cabeza
            self.Cabeza = nodoEliminar.Siguiente
            
            del nodoEliminar
            return

#%%
# Memoria dinámica

class Nodo:
    def __init__(self, Y, X):
        self.X = X
        self.Y = Y
        self.Siguiente = None

class Lista:
    def __init__(self):
        self.Cabeza = None
        self.Ultimo = None
        
    def insertarFinal(self, X, Y):
        nuevoNodo = Nodo(Y, X)
        if self.Cabeza is None:
            self.Cabeza = nuevoNodo
            self.Ultimo = nuevoNodo
        else:            
            self.Ultimo.Siguiente = nuevoNodo
            self.Ultimo = nuevoNodo
            
    def eliminarPrimero(self):
        if self.Cabeza is None:
            print("No hay elementos")
        else:
            nodoEliminar = self.Cabeza  
            self.Cabeza = nodoEliminar.Siguiente
            del nodoEliminar
#%%      
"""
insertar(L,X,Y,posicion)
    
    1. si p<= 0 ; return 0
    
    2. Crear un nuevo nodo
        nuevoNodo.X <-- T
        nuevoNodo.Y <-- T
        nuevoNodo.Siguiente <-- None
        
    3. Si p = 1
        nuevoNodo.Siguiente <-- 1.Cabeza
        L.Caveza = nuevoNOdo
        return 1
    
    4. Actual <-- L.Cabeza
        Contador + 1
    
    5. Mientrar Actual != Nulo AND Contador < p -1:
        Actual <-- Actual.Siguiente
        Contador += 1
        
        Si Actial = Nulo; print("Esa posicion no existe"); return 0
    
    6. nuevoNodo.Siguiente = Actual.Siguiente
        Actual.Siguiente = nuevoNodo

"""

"""
    def mostrar(self):
        
        elementos = []
"""

# Memoria estatica
class Lista:
    def __init__(self,capacidad=100):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.Ultimo = 0
    
    def agragar_elemento_final(self,e):
        
        if self.Ultimo >= self.capacidad:
            print("No queda espacio")
        
        else:           
        
        self.elementos[self.Ultimo]=e
        self.Ultimo += 1
        
    def insertar_elemento(self,e,posicion):
        if pos < 0:
            print("Posicion no valida")
        if self.Ultimo >= self.capacidad:
            print("No quedan huecos")
        
        i = self.Ultimo
        while i > posicion:
            self.elementos[i] = self.elementos[i - 1]
            i -=1
        
        self.elementos[posicion] = e
        self.Ultimo += 1
        

#%%

"""
Tipo Nodo:
    X <-- T
    Siguiente < -- int
    
Tipo Lista:
    vector[MAX] <-- Nodo
    Cabeza <-- int (indice al primer elemnto de la lista)
    Ultimo <-- int (indice al ultimo elemento de la lista)
    Tama;o <-- int
    ListaHuecos[MAX] <-- int (indices disponbles en el nodo)
    
InsertarFinal(L,e) --> NO CONOZCA LA REFERENCIA AL ULTIMO

    1. hueco <- DevuelveHuevco()
        Si hueco !=1 ; retunr 0
    
    2. L.vector[hueco.dato <-- nodo]
        L.vector[hueco.Siguiente = -1
    
    3. Si L.Cabeza == -1
        L.Cabeza = hueco
    
    4. actual <-- L.Cabeza
        MIentras L.vector[actual.Siguiente] != -1
            actual <- L.vector[actual].Siguiente
            
    5. L.vector[actual].Siguiente <-- hueco
    
    6. EliminarHueco()
"""



                
        
              
        

    
    
    