# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:11:13 2025

@author: Usuario

Control del timepo
"""
#Control del timepo
import time

contador = 0
tiempo_inicial = time.time()

# Es muy importante oner el contador
while contador < 100 :
    
    print(f"tiempo inicial: {tiempo_inicial}")
    print(f"tiempo actual: {time.time() }")
    print(f"tiempo transcurrido: {time.time() - tiempo_inicial}")
    time.sleep(1)
    
    if int(time.time() - tiempo_inicial) % 2 == 0:
        print("Aqui apilare un libro")
    if int(time.time() - tiempo_inicial) % 3 == 0:
        print("Aqui sacare un libro")        
        #en lugar de estos dos print debemos poner las funciones
    contador +=1
    
#%%
# Como poner los nombreas ramdom a los libros

import random

class libro:
    
    def _init(self):
        
        mylista = ["poesia","novela","articulo"]
        
        self.ISBN = None #random de 6 digitos numericos
        self.titulos = None #random de 10-20 digitos numericos IMPORT STRING pista ascii_letters
        self.genero = random.choice(mylista)
        self.paginas = None #random de 2 digitos numericos
        self.retraso = None  #random de booleanos

miLibro = libro()
    
print(miLibro.genero)

#%%
from abc import ABC, abstractclassmethod
import random
import string
import time

#INTERFAZ

class LibroGenerico(ABC):
    def __init__(self):
    
class PilaGenerica(ABC):
    def __init__(self):
    

#IMPLEMENTACION
class Libro(LibroGenerico):
    
class Pila(PilaGenerica):

def simulacion():
    
# MAIN

LibrosDevueltos = Pila()

while .....:
    
    print("1. Insertar....")
    print("2. Ordena....")
    print("3. Muestra.....")

opcion = int(input(......))
match option 
    case 1:
        LibrosDevueltos.apilar()
        
    case 2:
        
    
#%%