from zooAnimales.animal import Animal

class Pez (Animal):

    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def cantidadPeces():
        return len(Pez._listado)

    def movimiento():
        pass

    
    def crearSalmon(cls, nombre, edad,  genero):
        salmon = Pez(nombre, edad,"oceano", genero, "rojo", 6)
        cls.salmones += 1
        return salmon

    def crearBacalao(cls, nombre, edad,  genero):
        bacalo = Pez(nombre, edad,"oceano", genero, "gris", 6)  
        cls.bacalaos += 1
        return bacalo

    # setters and getters for colorEscamas, cantidadAletas and listado

    def setColorEscamas (self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getColorEscamas (self):
        return self._colorEscamas
    
    def setCantidadAletas (self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
    
    def getCantidadAletas (self):
        return self._cantidadAletas
    
    def setListado (self, listado):
        self._listado = listado
    
    def getListado (self):
        return self._listado

# La clase Pez tendrá algunos comportamientos particulares, en el
# atributo salmones y bacalaos se quiere llevar el conteo de veces
# que se usó el método crearSalmon y el método crearBacalao y el
# metodo cantidadPeces retornara la cantidad de peces
# creados en el sistema.

#  Para la clase Pez el método crearSalmon, creará un Pez con los
# valores para colorEscamas = “rojo”, cantidadAletas = 6 y hábitat
# = “oceano”, los demás valores los recibirá como parámetros.

#  Para la clase Pez el método crearBacalao, creará un Pez con
# los valores para colorEscamas = “gris”, cantidadAletas = 6 y
# hábitat = “oceano”, los demás valores los recibirá como
# parámetros.
    

