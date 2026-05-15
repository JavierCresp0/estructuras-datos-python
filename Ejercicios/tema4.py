# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 17:27:22 2025

@author: Usuario
"""

set = {1,2,3}
set.add(5)

class Conjunto:
    
    def __init__(self, bits = 8, value=0):
        self.max_bits = bits
        self.bits = value & ((1<<bits)-1) # esto limita "value" a 8 bits
        
    def __repr__(self):
        return f"{self.bits:0{self.max_bits}b}" #Para mostrar los bits en el print
    
    def union_conoperador(self,B):
        return Conjunto(self.max_bits, self.bits | B.bits)
    
    def union(self,B):
        
        result = 0
        for i in range(self.max_bits):
            a = (self.bits >> i) & 1
            b = (B.bits >> i) & 1
            
            result += (1 << i) * max(a,b)
        return Conjunto(self.max_bits,result)
    
    def inserseccion(self,B):
        
        result = 0
        for i in range(self.max_bits):
            a = (self.bits >> i) & 1
            b = (B.bits >> i) & 1
            
            result += (1 << i) * (a*b)
        return Conjunto(self.max_bits,result)
    
    def diferencia(self,B):
        
        result = 0
        for i in range(self.max_bits):
            a = (self.bits >> i) & 1
            b = (B.bits >> i) & 1
            
            if a and not b:
                result += (1 << i) 
                
        return Conjunto(self.max_bits,result)
        
A = Conjunto(8,25)
B = Conjunto(8,25)

C = A.union_conoperador(B)
print(A)

print(C)


### INTERSECCION Listas
"""
Estructura Nodo 
    dato = entero 
    siguiente = Nodo
fin Estructura

Estructura Conjunto
    cabeza = Nodo
fin estrutura

Funcion Union(A: Conjunto, B: Conjunto -> Conjunto C)

    C <- Conjunto()
    
    actual <- A.cabeza
    Mientras actual != None
        Agregar(C, actual.dato)
        actual <- actual.siguiente
    
    actual <- B.cabeza
    Mientras actual != Nove
        Si No Pertenece(C,actual.dato)
            Agregar(C, actual.dato)
        actual <- actual.siguiente
        
Recorrer 1 inical A, 1 vez B (N veces C)

// Ahora si la lista estubiera ordenada

Funcion Union_Ordenada(A: Conjunto, B: Conjunto) --> Conjunto: C

    C <- Conjunto()
    ptrA <- A.cabeza
    ptrB <- B.cabeza
    
    Mientras punteo/ptroA != None o prtroB != None
    
        Si ptrA = None // Si A esta vacio C sera todo B
            Agregar(C, ptrB.dato)
            ptrB <- ptrB.siguiente
            
        Sino ptrB = None
            Agregar(C, ptrA.dato)
            ptrB <- ptrA.siguiente
        
        Sino Si ptrA.dato < ptrB.dato
            Agregar(C,ptrA.dato)
            ptrA <- ptrA.siguiente
        
        Sino Si ptrB.dato < ptrA.dato
            Agragar(C, ptrB.dato)
            ptrB <- ptrB.siguiente
            
        Sino 
            Agregar(C, ptrA.dato)
            ptrA <- ptrA.siguiente
            ptrA <- ptrb.siguiente
        
"""