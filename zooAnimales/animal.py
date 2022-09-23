from zona import Zona

class Animal (Zona):
    _totalAnimales = 0
    def __init__ (self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad =  edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        __totalAnimales += 1
    
    def movimiento ():
        pass

    def totalPorTipo ():
        pass

    def __str__(self):
        pass

    def setNombre (self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre

    def setEdad (self, edad):
        self._edad = edad

    def getEdad (self):
        return self._edad

    #Create setter and getter for habitat, genero and zona
    def setHabitat (self, habitat):
        self._habitat = habitat
    
    def getHabitat (self):
        return self._habitat

    def setGenero (self, genero):
        self._genero = genero

    def getGenero (self):
        return self._genero

    def setZona (self, zona):
        self._zona = zona
    
    def getZona (self):
        return self._zona
    

    