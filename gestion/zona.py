from zoologico import Zoologico

class Zona (Zoologico): 
    def __init__(self, nombre, zoo):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def agregarAnimales():
        pass

    def cantidadTotalAnimales():
        pass

    # setters and getters for nombre, zoo and animales
    def setNombre (self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre
    
    def setZoo (self, zoo):
        self._zoo = zoo
    
    def getZoo (self):
        return self._zoo
    
    def setAnimales (self, animales):
        self._animales = animales
    
    def getAnimales (self):
        return self._animales
