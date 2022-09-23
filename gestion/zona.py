class Zona (): 
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
    
    def agregarAnimales(self, animal):
        Zona._animales.append(animal)
        

    def cantidadTotalAnimales():
        return len(Zona._animales)

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
    
# Para la clase Zona el método agregarAnimales añadira un nuevo animal al listado
# de animales y el método cantidadAnimales retornara la cantidad de animales en la
# zona
