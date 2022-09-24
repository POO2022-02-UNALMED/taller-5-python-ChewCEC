from zooAnimales.animal import Animal

class Reptil (Animal):

    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    def cantidadReptiles ():
        return len(Reptil._listado)

    def movimiento():
        pass
    
    @classmethod
    def crearIguana (cls, nombre, edad, genero):
        cls.iguanas += 1
        iguanas = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        return iguanas

    @classmethod
    def crearSerpiente (cls, nombre, edad, genero):
        cls.serpientes += 1
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        return serpiente

# setters and getters for largoCola and listado and colorEscamas
    def setLargoCola (self, largoCola):
        self._largoCola = largoCola

    def getLargoCola (self):
        return self._largoCola

    def setListado (self, listado):
        self._listado = listado
    
    def getListado (self):
        return self._listado

    def setColorEscamas (self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getColorEscamas (self):
        return self._colorEscamas

    
# La clase Reptil tendrá algunos comportamientos particulares, en
# el atributo iguanas y serpientes se quiere llevar el conteo de
# veces que se usó el método crearIguana y el método
# crearSerpiente y el metodo cantidadReptiles retornara la
# cantidad de reptiles creados en el sistema.

#  Para la clase Reptil el método crearIguana, creará un Reptil
# con los valores para colorEscamas = “verde”, largoCola = 3 y
# hábitat = “humedal”, los demás valores los recibirá como
# parámetros.

#  Para la clase Reptil el método crearSerpiente, creará un Reptil
# con los valores para colorEscamas = “blanco”, largoCola = 1 y
# hábitat = “jungla”, los demás valores los recibirá como
# parámetros.