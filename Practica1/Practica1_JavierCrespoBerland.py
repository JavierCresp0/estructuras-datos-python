# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:10:29 2025

@author: Usuario
"""
from abc import ABC, abstractmethod
import time
import random
import string


# INTERFAZ
class LibroGenerico(ABC):
    @abstractmethod
    def __init__(self,Siguiente, ISBN, titulo, paginas, genero, retraso):
        pass

class PilaGenerica(ABC):
    @abstractmethod
    def apilar(self, libro):
        pass
    

    @abstractmethod
    def desapilar(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass
    
    @abstractmethod
    def proximo(self):
        pass


# IMPLEMENTACIÓN

class Libro(LibroGenerico):
    def __init__(self):

        generos = ["ensayo", "novela", "poesía"]
        self.Siguiente = None
        self.ISBN = random.randint(100000, 999999)  # 6 dígitos
        longitud_titulo = random.randint(10, 20)
        self.titulo = ''.join(random.choices(string.ascii_letters, k=longitud_titulo))
        self.genero = random.choice(generos)
        self.paginas = random.randint(10, 99)  # 2 dígitos
        self.retraso = random.choice([True, False])
        

        
    def mostrar(self):
        print("ISBN del libro:", self.ISBN)
        print("Título del libro:", self.titulo)
        print("Género del libro:", self.genero)
        print("Número de páginas del libro:", self.paginas)
        print("Retraso del libro:", self.retraso)






class Pila(PilaGenerica):
    def __init__(self):
        self.Cabeza = None  # El tope de la pila será un objeto Libro

    def apilar(self, libro):
        # Enlaza el libro actual al que ya estaba en la cabeza
        libro.Siguiente = self.Cabeza
        self.Cabeza = libro

    def desapilar(self):
        if self.Cabeza is None:
            print("La pila está vacía.")
            return None
        libro_eliminado = self.Cabeza
        self.Cabeza = libro_eliminado.Siguiente
        libro_eliminado.Siguiente = None
        return libro_eliminado

    def mostrar(self):
        if self.Cabeza is None:
            print("La pila está vacía.")
            return
        actual = self.Cabeza
        while actual:
            print(actual.ISBN, end="")
            if actual.Siguiente:
                print(", ", end="")
            actual = actual.Siguiente
        print()  # Salto de línea final


    def proximo(self):
        if self.Cabeza is None:
            print("La pila está vacía.")
            return None
        return self.Cabeza

# Función para mostrar pilas
def pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia):
    print("\nPila de LibrosDevueltos:",end="")
    LibrosDevueltos.mostrar()
    print("\nPila Ensayo:",end="")
    pila_ensayo.mostrar()
    print("\nPila Novela:",end="")
    pila_novela.mostrar()
    print("\nPila Poesía:",end="")
    pila_poesia.mostrar()
    print()  # Salto de línea final
    

def simulacion(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia):  

    tiempo_inicial = time.time()

    # Simulación durante 30 ciclos 
    while time.time() - tiempo_inicial < 30:
        tiempo_actual = time.time()
        tiempo_transcurrido = int(tiempo_actual - tiempo_inicial)
        print(f"\nTiempo transcurrido: {tiempo_transcurrido} segundos")
        time.sleep(1)
        
        # Cada 2 segundos se simula la devolución de un libro
        if tiempo_transcurrido % 2 == 0:
            libro = Libro()
            LibrosDevueltos.apilar(libro)
            print("--------------------------------------------------------------------------.")
            pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
            print(f"Evento: El libro con ISBN {libro.ISBN} ha sido devuelto.")
            print("--------------------------------------------------------------------------.")
        
        # Cada 3 segundos se simula la ordenación de un libro
        if tiempo_transcurrido % 3 == 0:
            libro = LibrosDevueltos.desapilar()
            if libro:
                if libro.genero == "ensayo":
                    pila_ensayo.apilar(libro)
                    print("--------------------------------------------------------------------------.")
                    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                    print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Ensayo.")
                    if libro.retraso:
                        print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                    print("--------------------------------------------------------------------------.")
                elif libro.genero == "novela":
                    pila_novela.apilar(libro)
                    print("--------------------------------------------------------------------------.")
                    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                    print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Novela.")
                    if libro.retraso:
                        print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                    print("--------------------------------------------------------------------------.")
                elif libro.genero == "poesía":
                    pila_poesia.apilar(libro)
                    print("--------------------------------------------------------------------------.")
                    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                    print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Poesía.")
                    if libro.retraso:
                        print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                    print("--------------------------------------------------------------------------.")

    # Fase 2: Biblioteca cerrada    
    print("\n--- Fase 2: Biblioteca cerrada, iniciando ordenación final ---")
    tiempo_inicial2 = time.time()

    # Mientras haya algún libro en cualquier pila
    while (LibrosDevueltos.Cabeza is not None or 
           pila_ensayo.Cabeza is not None or 
           pila_novela.Cabeza is not None or 
           pila_poesia.Cabeza is not None):
        tiempo_transcurrido2 = int(time.time() - tiempo_inicial2)
        print(f"\nFase 2 - Tiempo transcurrido: {tiempo_transcurrido2} segundos")
        time.sleep(1)

        
        # Procesa un libro de LibrosDevueltos cada 1 segundo
        if tiempo_transcurrido2 % 1 == 0:
            if LibrosDevueltos.Cabeza is not None:
                libro = LibrosDevueltos.desapilar()
                if libro:
                    if libro.genero == "ensayo":
                        pila_ensayo.apilar(libro)
                        print("--------------------------------------------------------------------------.")
                        pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                        print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Ensayo.")
                        if libro.retraso:
                            print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                        print("--------------------------------------------------------------------------.")
                    elif libro.genero == "novela":
                        pila_novela.apilar(libro)
                        print("--------------------------------------------------------------------------.")
                        pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                        print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Novela.")
                        if libro.retraso:
                            print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                        print("--------------------------------------------------------------------------.")
                    elif libro.genero == "poesía":
                        pila_poesia.apilar(libro)
                        print("--------------------------------------------------------------------------.")
                        pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                        print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Poesía.")
                        if libro.retraso:
                            print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                        print("--------------------------------------------------------------------------.")



        # Procesa un libro de una pila de género cada 2 segundos
        if tiempo_transcurrido2 % 2 == 0:
            pilas_genero = [pila for pila in [pila_ensayo, pila_novela, pila_poesia] if pila.Cabeza is not None]

            if pilas_genero:
                pila_elegida = random.choice(pilas_genero)

                print("--------------------------------------------------------------------------.")
                pilas(LibrosDevueltos, pila_ensayo, pila_novela, pila_poesia)

                if pila_elegida is pila_ensayo:
                    print(f"Evento: El libro con ISBN {pila_ensayo.Cabeza.ISBN} abandona la pila Ensayo.")
                    pila_ensayo.desapilar()
                elif pila_elegida is pila_novela:
                    print(f"Evento: El libro con ISBN {pila_novela.Cabeza.ISBN} abandona la pila Novela.")
                    pila_novela.desapilar()
                else:
                    print(f"Evento: El libro con ISBN {pila_poesia.Cabeza.ISBN} abandona la pila Poesía.")
                    pila_poesia.desapilar()

                print("--------------------------------------------------------------------------.")              


        time.sleep(0.1)  # Pequeño retardo 

    print("\n--- Ordenación final completada: Todas las pilas están vacías ---")
    print("\nEstado final de las pilas:")
    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia) 

            



# MAIN

LibrosDevueltos = Pila()
pila_ensayo = Pila()
pila_novela = Pila()
pila_poesia = Pila()

while True:
    print("\nMenú Principal")
    print("1. Devolver un libro a la pila de LibrosDevueltos")
    print("2. Ordenar un libro de LibrosDevueltos a su pila de género")
    print("3. Imprimir la pila LibrosDevueltos")
    print("4. Imprimir una de las pilas de género: 1,2,3")
    print("5. Ver información sobre el próximo libro a ordenar de LibrosDevueltos")
    print("6. Iniciar la simulación")
    print("7. Salir de la aplicación")

    opcion = input("Elige una opción: ")

    match opcion:
        
        case "1":
            
            libro = Libro()
            LibrosDevueltos.apilar(libro)            
            print("--------------------------------------------------------------------------.")
            pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
            print(f"Evento: El libro con ISBN {libro.ISBN} ha sido devuelto.")
            print("--------------------------------------------------------------------------.")
        
        case "2":
            print("\n2. Ordenar un libro de LibrosDevueltos a su pila de género")
            libro = LibrosDevueltos.desapilar()
            if libro:
                if libro.genero == "ensayo":
                    pila_ensayo.apilar(libro)
                    print("--------------------------------------------------------------------------.")
                    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                    print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Ensayo.")
                    if libro.retraso:
                        print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                    print("--------------------------------------------------------------------------.")
                elif libro.genero == "novela":
                    pila_novela.apilar(libro)
                    print("--------------------------------------------------------------------------.")
                    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                    print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Novela.")
                    if libro.retraso:
                        print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                    print("--------------------------------------------------------------------------.")
                elif libro.genero == "poesía":
                    pila_poesia.apilar(libro)
                    print("--------------------------------------------------------------------------.")
                    pilas(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
                    print(f"Evento: El libro con ISBN {libro.ISBN} se ha ordenado en la pila Poesía.")
                    if libro.retraso:
                        print(f"Mensaje: El libro con ISBN {libro.ISBN} se ha devuelto con retraso.")
                    print("--------------------------------------------------------------------------.")
        
        case "3":
            print("--------------------------------------------------------------------------.")
            print("\nPila de LibrosDevueltos:",end="")
            LibrosDevueltos.mostrar()
            print("--------------------------------------------------------------------------.")
            
        case "4":
            print("\nPresiona 1-Ensayo")
            print("Presiona 2-Novela ")
            print("Presiona 3-Poesía ")
            
            opcion2 = input("Elige una opción: ")

            match opcion2:
                
                case "1":
                    print("--------------------------------------------------------------------------.")
                    print("\nPila Ensayo:",end="")
                    pila_ensayo.mostrar()
                    print("--------------------------------------------------------------------------.")
                    
                case "2":
                    print("--------------------------------------------------------------------------.")
                    print("\nPila Novela:",end="")
                    pila_novela.mostrar()
                    print("--------------------------------------------------------------------------.")
                    
                case "3":
                    print("--------------------------------------------------------------------------.")
                    print("\nPila Poesía:",end="")
                    pila_poesia.mostrar()
                    print("--------------------------------------------------------------------------.")                 
        
        case "5":
            print("\n--------------------------------------------------------------------------.")
            if LibrosDevueltos.Cabeza is None:
                print("La pila está vacía.")
            else:
                LibrosDevueltos.Cabeza.mostrar()
            print("--------------------------------------------------------------------------.")
            
        
        case "6":
            simulacion(LibrosDevueltos,pila_ensayo,pila_novela,pila_poesia)
            
        case "7":
            print("Saliendo...")
            break        

        case _:
            print("\nOpción no válida.")