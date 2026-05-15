# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:07:46 2025

@author: Usuario
"""
"""
class Usuario :
    def __init__(self, user, password):
        self.user= user
        self.__password= password
        
    def obtener_usuario(self):
        return self.user
    
    def recuperar_password(self,email):
        if email == "edemplo":
            return self.__password
    
       
user1= Usuario("martin","12345")
#user2= Usuario(user="martin", password="12345")
    
print(f"la contraseña es: {recupera}")


class Administrador(Usuario):
    def __init__(self, user, password, seccion):
        super().__init__(user, password)
        self.seccion = seccion

    def actualizar_usuario(self, usuario_objetivo, nueva_password):
            usuario_objetivo._Usuario_password = nueva_password

adm = Administrador("jose","qwerty",2)

adm.actualizar_usuario(user1, "cambiada")

print(f"La contrase;a a cambiado a"{user1.obtener_usuario()})

"""
#%%
from abc import ABC, abstractclassmethod

class Vehiculo(ABC):
    def __init__(self,color,electrico,marca):
        self.color = color
        self.electrico = electrico
        self.marca = marca
    
    @abstractclassmethod
    def arrancar(self):
        pass
        
    @abstractclassmethod
    def obtener(self):
        pass
    
    

class Tesla(Vehiculo):
    def __init__(self,color,electrico,marca):
        super.__init__(color,electrico,"Tesla")
        
    def arrancar(self):
        print("Soy un tesla y voy volando")
       
        
class Renault(Vehiculo):
    def __init__(self,color,electrico,marca):
        super.__init__(color,electrico,"Renault")
        
    def arrancar(self):
        print("Soy un Renault y voy andando")
       

a = Tesla("rojo",True)
        #Es normal el error pues los metodos abstractos obligan a sus clase hijas
        # a tenerlo y no tienen obtener

#%%
from abc import ABC, abstractclassmethod        

class Documento(ABC):
    def __init__(self,nombre,formato,peso):        
        self.nombre= nombre
        self.formato = formato
        self.peso = peso
    
    @abstractclassmethod
    def procesar(self):
        pass
        
    @abstractclassmethod
    def comprimir(self):
        pass
    
    @abstractclassmethod
    def descomprimir(self):
        pass
    
    @abstractclassmethod
    def enviar(self):
        pass
    
    
class Texto(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")


class Imagen(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")


class Audio(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")
        

class Video(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")
    

documentos = [
    Texto("texto", "txt", 20)
    Video("Video", "mp4", 10)
]

for doc in documentos:
    print(f"Procesando documento: {doc.nombre} ({doc.formato} - {doc.peso})")
    print(doc.porcesar())
    print



#%%

from abc import ABC, abstractclassmethod        

class Documento(ABC):
    def __init__(self,nombre,formato,peso):        
        self.nombre= nombre
        self.formato = formato
        self.peso = peso
    
    @abstractclassmethod
    def procesar(self):
        pass
        
    @abstractclassmethod
    def comprimir(self):
        pass
    
    @abstractclassmethod
    def descomprimir(self):
        pass
    
    @abstractclassmethod
    def enviar(self):
        pass


class Nuevo(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)    

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")
        
    
class Texto(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")


class Imagen(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")


class Audio(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")
        

class Video(Documento):
    def __init__(self,nombre,formato,peso):
        super.__init__(nombre,formato,peso)
        

    def procesar(self):
        print("El documento de texto")
        

    def comprimir(self):
        print("El documento texto comprimido")

    def descomprimir(self):
        print("El documento texto descomprimido")
    

    def enviar(self):
        print("El documento texto enviado")
        
#%%

match case 

# debo hacer con esto el menu de la practica 1