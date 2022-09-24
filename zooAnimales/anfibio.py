from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def cantidadAnfibios():
        return len(Anfibio._listado)

    def movimiento():
        pass

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas += 1

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.__init__(nombre, edad, "selva", genero, "negro y amarillo", False)

# Para la clase Anfibio el método crearRana, creará un Anfibio
# con los valores para colorPiel = “rojo”, venenoso = true y hábitat
# = “selva”, los demás valores los recibirá como parámetros.
#  Para la clase Anfibio el método crearSalamandra, creará un
# Anfibio con los valores para colorPiel = “negro y amarillo”,
# venenoso = false y hábitat = “selva”, los demás valores los recibirá
# como parámetros.

    
    # setters and getters for colorPiel, venenoso and listado
    def setColorPiel (self, colorPiel):
        self._colorPiel = colorPiel
    
    def getColorPiel (self):
        return self._colorPiel

    def setVenenoso (self, venenoso):
        self._venenoso = venenoso

    def getVenenoso (self):
        return self._venenoso

    def setListado (self, listado):
        self._listado = listado
    
    def getListado (self):
        return self._listado