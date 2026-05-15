# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:46:37 2025

@author: Usuario
"""

from abc import ABC, abstractmethod
import time
import random
import string


# INTERFAZ
class LibroGenerico(ABC):
    @abstractmethod
    def __init__(self, ISBN, titulo, paginas, genero, retraso):
        pass

class ArbolGenerico(ABC):    

    @abstractmethod
    def insertar(self):
        pass

    @abstractmethod
    def insertar_recursivo(self):
        pass
    
    #INORDER
    @abstractmethod
    def recorrer_inorder(self):
        pass
    
    @abstractmethod
    def recorrer_inorder_recursivo(self):
        pass  
    
    
    #PREORDER
    @abstractmethod
    def recorrer_preorder(self):
        pass

    @abstractmethod
    def recorrer_preorder_recursivo(self, libro_actual, resultado):
        pass
    
    #POSTORDER
    @abstractmethod
    def recorrer_postorder(self):
        pass
    
    @abstractmethod
    def recorrer_postorder_recursivo(self, libro_actual, resultado):
        pass
    
    @abstractmethod
    def borrar(self,ISBN_Borrar):
        pass
    
    @abstractmethod
    def borrar_recursivo(self,libro_actual,ISBN_Borrar):
        pass
    
    @abstractmethod
    def buscar(self, isbn):
        pass

    @abstractmethod
    def _buscar_recursivo(self, nodo, isbn):
        pass


# IMPLEMENTACIÓN
class Libro(LibroGenerico):
    def __init__(self):
        generos = ["ensayo", "novela", "poesía"]
        self.derecha = None
        self.izquierda = None
        self.ISBN = random.randint(100000, 999999)  # 6 dígitos
        longitud_titulo = random.randint(10, 20)
        self.titulo = ''.join(random.choices(string.ascii_letters, k=longitud_titulo))
        self.genero = random.choice(generos)
        self.paginas = random.randint(10, 99)  # 2 dígitos
        self.retraso = random.choice([True, False])

class Arbol(ArbolGenerico):
    def __init__(self):
        self.raiz=None
    
    def insertar(self,Libro):
        self.raiz = self.insertar_recursivo(self.raiz,Libro)
    
    def insertar_recursivo(self,actual,Libro):
        if actual is None:
            return Libro
        else:
            if(Libro.ISBN > actual.ISBN):
                actual.derecha = self.insertar_recursivo(actual.derecha,Libro)
            elif(Libro.ISBN < actual.ISBN):
                actual.izquierda = self.insertar_recursivo(actual.izquierda,Libro)
            return actual
    
    #INORDER
    def recorrer_inorder(self):
        if self.raiz is None:
            print("El Árbol está vacío.")
            return None
        
        resultado = []
        self.recorrer_inorder_recursivo(self.raiz, resultado)
        print(", ".join(str(isbn) for isbn in resultado))
    
    def recorrer_inorder_recursivo(self, libro_actual, resultado):
        if libro_actual:
            self.recorrer_inorder_recursivo(libro_actual.izquierda, resultado)
            resultado.append(libro_actual.ISBN)
            self.recorrer_inorder_recursivo(libro_actual.derecha, resultado)
        return
    
    #PREORDER
    def recorrer_preorder(self):
        if self.raiz is None:
            print("El Árbol está vacío.")
            return None
        
        resultado = []
        self.recorrer_preorder_recursivo(self.raiz, resultado)
        print(", ".join(str(isbn) for isbn in resultado))
    
    def recorrer_preorder_recursivo(self, libro_actual, resultado):
        if libro_actual:
            resultado.append(libro_actual.ISBN)
            self.recorrer_preorder_recursivo(libro_actual.izquierda, resultado)
            self.recorrer_preorder_recursivo(libro_actual.derecha, resultado)
        return
    
    #POSTORDER
    def recorrer_postorder(self):
        if self.raiz is None:
            print("El Árbol está vacío.")
            return None
        
        resultado = []
        self.recorrer_postorder_recursivo(self.raiz, resultado)
        print(", ".join(str(isbn) for isbn in resultado))
    
    def recorrer_postorder_recursivo(self, libro_actual, resultado):
        if libro_actual:
            self.recorrer_postorder_recursivo(libro_actual.izquierda, resultado)
            self.recorrer_postorder_recursivo(libro_actual.derecha, resultado)
            resultado.append(libro_actual.ISBN)
        return
    
    def borrar(self,ISBN_Borrar):
        self.raiz = self.borrar_recursivo(self.raiz,ISBN_Borrar)
    
    def borrar_recursivo(self,libro_actual,ISBN_Borrar):
        if libro_actual is None:
            return libro_actual
        else:
            if ISBN_Borrar > libro_actual.ISBN:
                libro_actual.derecha = self.borrar_recursivo(libro_actual.derecha,ISBN_Borrar)
            elif ISBN_Borrar < libro_actual.ISBN:
                libro_actual.izquierda = self.borrar_recursivo(libro_actual.izquierda,ISBN_Borrar)
        
  
            #Caso 1
            else:                
                if libro_actual.izquierda is None and libro_actual.derecha is None:
                    return None
                
                #Caso 2
                if libro_actual.izquierda is None:
                    return libro_actual.derecha
                elif libro_actual.derecha is None:
                    return libro_actual.izquierda
        
                #Caso 3
                # Se busca el sucesor inorden (mínimo del subárbol derecho)
                encontrado = libro_actual.derecha
                while encontrado.izquierda is not None:
                    encontrado = encontrado.izquierda                
                # Se actualizan los datos del nodo actual con los del sucesor
                libro_actual.ISBN = encontrado.ISBN
                libro_actual.titulo = encontrado.titulo
                libro_actual.paginas = encontrado.paginas
                libro_actual.genero = encontrado.genero
                libro_actual.retraso = encontrado.retraso
                # Se elimina el nodo duplicado en el subárbol derecho
                libro_actual.derecha = self.borrar_recursivo(libro_actual.derecha, encontrado.ISBN)
        
        return libro_actual
    
    def buscar(self, isbn):
        resultado = self._buscar_recursivo(self.raiz, isbn) 
        
        if resultado:
            return True
        else:
            return False

    def _buscar_recursivo(self, nodo, isbn):
        # Si llegamos a un nodo nulo, significa que no se encontró el elemento
        if nodo is None:
            return None
  
        if nodo.ISBN == isbn:
            return nodo
        # Si el ISBN buscado es menor que el del nodo actual, buscamos en el subárbol izquierdo
        if isbn < nodo.ISBN:
            return self._buscar_recursivo(nodo.izquierda, isbn)
        # Si el ISBN buscado es mayor, lo buscamos en el subárbol derecho
        else:
            return self._buscar_recursivo(nodo.derecha, isbn)
        

def simulacion(ABB1,ABB2,ABB3):  

    tiempo_inicial = time.time()

    # Simulación durante 60 csec
    while time.time() - tiempo_inicial < 60:
        tiempo_actual = time.time()
        tiempo_transcurrido = int(tiempo_actual - tiempo_inicial)
        print(f"\nTiempo transcurrido: {tiempo_transcurrido} segundos")
        time.sleep(1)
        
        # Cada 5 segundos se simula la devolución de un libro
        if tiempo_transcurrido != 0 and tiempo_transcurrido % 5 == 0:
            print("--------------------------------------------------------------------------.")
            libro = Libro()
            if libro.genero == "ensayo":
                ABB1.insertar(libro)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB1.")
            elif libro.genero == "novela":
                ABB2.insertar(libro)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB2.")
            else:
                ABB3.insertar(libro)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB3.")
            print("--------------------------------------------------------------------------.")
        
        # Cada 7 segundos se detecta retraso de un libro
        if tiempo_transcurrido != 0 and tiempo_transcurrido % 7 == 0:
            print("--------------------------------------------------------------------------")
        
            # Se escoge aleatoriamente uno de los tres árboles.
            arboles_con_libros = [arbol for arbol in [ABB1, ABB2, ABB3] if arbol.raiz is not None]
            arbol_seleccionado = random.choice(arboles_con_libros)
            
            # Se obtiene la lista de nodos (libros) en el árbol seleccionado
            nodos = obtener_nodos(arbol_seleccionado.raiz)  
            
            if nodos:
                libro_seleccionado = random.choice(nodos)
                
                if libro_seleccionado.retraso:
                    print("--------------------------------------------------------------------------.")
                    if libro_seleccionado.genero == "ensayo":
                        arbol_seleccionado.borrar(libro_seleccionado.ISBN)
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Se detecta retraso en la devolución del libro {libro_seleccionado.ISBN} del ABB1.")
                        print("--------------------------------------------------------------------------.")
                    elif libro_seleccionado.genero == "novela":
                        arbol_seleccionado.borrar(libro_seleccionado.ISBN)
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Se detecta retraso en la devolución del libro {libro_seleccionado.ISBN} del ABB2.")
                        print("--------------------------------------------------------------------------.")
                    else:
                        arbol_seleccionado.borrar(libro_seleccionado.ISBN)
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Se detecta retraso en la devolución del libro {libro_seleccionado.ISBN} del ABB3.")
                        print("--------------------------------------------------------------------------.")
                else:
                    arboles(ABB1,ABB2,ABB3)
                    print(f"NO se detecta retraso en el libro {libro_seleccionado.ISBN}.")
                    print("--------------------------------------------------------------------------.")
    print("\n******************************************************************")
    print("*                                                                *")
    print("*                  ¡Simulación finalizada!                       *")
    print("*                                                                *")
    print("******************************************************************")
                    
        
        
def obtener_nodos(nodo):
    return [] if nodo is None else [nodo] + obtener_nodos(nodo.izquierda) + obtener_nodos(nodo.derecha)

# Función para mostrar los Arboles
def arboles(ABB1,ABB2,ABB3):
    print("ABB1:",end="")
    ABB1.recorrer_inorder()
    print("\nABB2:",end="")
    ABB2.recorrer_inorder()
    print("\nABB3:",end="")
    ABB3.recorrer_inorder()
    print()  # Salto de línea final
    
# MAIN

ABB1 = Arbol()
ABB2 = Arbol()
ABB3 = Arbol()

while True:
    print("\nMenú Principal")
    print("1. Insertar un libro en un ABB")
    print("2. Buscar cualquier libro en un ABB")
    print("3. Imprimir lista de libros en cualquier ABB")
    print("4. Borrar un libro introducido por teclado")
    print("5. Introducir un número y crear dicha cantidad de libros")
    print("6. Introducir un número y generar al azar dicha cantidad de libros, que se borrarán, si existen")
    print("7. Iniciar la simulación")
    print("8. Salir de la aplicación")

    opcion = input("Elige una opción: ")

    match opcion:
        
        case "1":            
            libro = Libro()
            
            while True:
                numero = input("\nIntroduce el ISBN (número de 6 dígitos): ")
                try:
                    numero = int(numero)
                    if 100000 <= numero <= 999999:
                        libro.ISBN = numero                        
                        break  
                    else:
                        print("El ISBN debe tener exactamente 6 dígitos.")
                except ValueError:                    
                    print("Eso no es un número válido.")
                    
            print("\n--------------------------------------------------------------------------.")
            if libro.genero == "ensayo":
                ABB1.insertar(libro)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB1.")
            elif libro.genero == "novela":
                ABB2.insertar(libro)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB2.")
            else:
                ABB3.insertar(libro)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB3.")
            print("--------------------------------------------------------------------------.")
        
        case "2":
            
            while True:
                buscar = input("\nIntroduce el ISBN del libro a buscar: ")
                try:
                    buscar = int(buscar)
                    if 100000 <= buscar <= 999999:                                                
                        break  
                    else:
                        print("El ISBN debe tener exactamente 6 dígitos.")
                except ValueError:                    
                    print("Eso no es un número válido.")
        
          
            print("\n--------------------------------------------------------------------------.")
            if ABB1.buscar(buscar):
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro encontrado: ISBN {buscar} en ABB1")
            elif ABB2.buscar(buscar):
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro encontrado: ISBN {buscar} en ABB2")
            elif ABB3.buscar(buscar):
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro encontrado: ISBN {buscar} en ABB3")
            else:
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro con ISBN {buscar} no encontrado.")
            print("--------------------------------------------------------------------------.")
        case "3":
            print("\nPresiona 1-Ensayo")
            print("Presiona 2-Novela ")
            print("Presiona 3-Poesía ")
            
            opcion2 = input("Elige una opción: ")

            match opcion2:
                
                case "1":
                    print("--------------------------------------------------------------------------.")
                    print("ABB1 INORDER:",end="")
                    ABB1.recorrer_inorder()
                    print()  # Salto de línea final
                    print("ABB1 PREORDER:",end="")
                    ABB1.recorrer_preorder()
                    print()  # Salto de línea final
                    print("ABB1 POSTORDEN:",end="")
                    ABB1.recorrer_postorder()   
                    print("--------------------------------------------------------------------------.")
                    
                case "2":
                    print("--------------------------------------------------------------------------.")
                    print("ABB2 INORDER:",end="")
                    ABB2.recorrer_inorder()
                    print()  # Salto de línea final
                    print("ABB2 PREORDER:",end="")
                    ABB2.recorrer_preorder()
                    print()  # Salto de línea final
                    print("ABB2 POSTORDEN:",end="")
                    ABB2.recorrer_postorder()
                    print("--------------------------------------------------------------------------.")
                    
                case "3":
                    print("--------------------------------------------------------------------------.")
                    print("ABB3 INORDER:",end="")
                    ABB3.recorrer_inorder()
                    print()  # Salto de línea final
                    print("ABB3 PREORDER:",end="")
                    ABB3.recorrer_preorder()
                    print()  # Salto de línea final
                    print("ABB3 POSTORDEN:",end="")
                    ABB3.recorrer_postorder()
                    print("--------------------------------------------------------------------------.")
            
        case "4":
            while True:
                borrar = input("\nIntroduce el ISBN del libro a borrar: ")
                try:
                    borrar = int(borrar)
                    if 100000 <= borrar <= 999999:                                                
                        break  
                    else:
                        print("El ISBN debe tener exactamente 6 dígitos.")
                except ValueError:                    
                    print("Eso no es un número válido.")
             
            print("--------------------------------------------------------------------------.")
            if ABB1.buscar(borrar):
                ABB1.borrar(borrar)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro encontrado y BORRADO con ISBN {borrar} en ABB1")
            elif ABB2.buscar(borrar):
                ABB2.borrar(borrar)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro encontrado y BORRADO con ISBN {borrar} en ABB2")
            elif ABB3.buscar(borrar):
                ABB3.borrar(borrar)
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro encontrado y BORRADO con ISBN {borrar} en ABB3")
            else:
                arboles(ABB1,ABB2,ABB3)
                print(f"Evento: Libro con ISBN {borrar} no encontrado.")
            print("--------------------------------------------------------------------------.")

        case "5":
            while True:
                numero = input("\nIntroduce el ISBN de libros a crear: ")
                try:
                    numero = int(numero)
                    if 0 < numero:                                                
                        break  
                    else:
                        print("El número de libros tiene que ser mayor a 0.")
                except ValueError:                    
                    print("Eso no es un número válido.")
            
            for i in range(numero):
                libro = Libro()
                
                print("\n--------------------------------------------------------------------------.")
                if libro.genero == "ensayo":
                    ABB1.insertar(libro)
                    arboles(ABB1,ABB2,ABB3)
                    print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB1.")
                    print("--------------------------------------------------------------------------.")
                elif libro.genero == "novela":
                    ABB2.insertar(libro)
                    arboles(ABB1,ABB2,ABB3)
                    print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB2.")
                    print("--------------------------------------------------------------------------.")
                else:
                    ABB3.insertar(libro)
                    arboles(ABB1,ABB2,ABB3)
                    print(f"Evento: Se devuelve el libro con id {libro.ISBN} al ABB3.")
                    print("--------------------------------------------------------------------------.")
                time.sleep(1)  # Pequeño retardo 
            
            
        
        case "6":
            
            while True:
                numero = input("\nIntroduce el número de libros a crear: ")
                try:
                    numero = int(numero)
                    if 0 < numero:                                                
                        break  
                    else:
                        print("El número de libros tiene que ser mayor a 0.")
                except ValueError:                    
                    print("Eso no es un número válido.")
           
            for i in range(numero):
                libro = Libro()
                
                print("\n--------------------------------------------------------------------------.")
                if libro.genero == "ensayo":
                    if ABB1.buscar(libro.ISBN):
                        ABB1.borrar(libro.ISBN)
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Evento: Libro encontrado y BORRADO: ISBN {libro.ISBN} en ABB1")
                    else: 
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Evento: No se encontró el libro con id {libro.ISBN} en ABB1.")
                    print("--------------------------------------------------------------------------.")
                elif libro.genero == "novela":
                    if ABB2.buscar(libro.ISBN):
                        ABB2.borrar(libro.ISBN)
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Evento: Libro encontrado y BORRADO: ISBN {libro.ISBN} en ABB2")
                    else:   
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Evento: No se encontró el libro con id {libro.ISBN} en ABB2.")
                    print("--------------------------------------------------------------------------.")
                else:
                    if ABB3.buscar(libro.ISBN):
                        ABB3.borrar(libro.ISBN)
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Evento: Libro encontrado y BORRADO: ISBN {libro.ISBN} en ABB3")
                    else:   
                        arboles(ABB1,ABB2,ABB3)
                        print(f"Evento: No se encontró el libro con id {libro.ISBN} en ABB3.")
                    print("--------------------------------------------------------------------------.")
               # time.sleep(1)  # Pequeño retardo 
            
        case "7":
            simulacion(ABB1,ABB2,ABB3)
        
        case "8":
            print("Saliendo...")
            break
        

        case _:
            print("\nOpción no válida.")


